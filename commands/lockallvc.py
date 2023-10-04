import discord
from discord.ext import commands
from discord.embeds import Embed
from json import load
from extras.directory import Path
from extras.permissions import *


class LockAllVc(commands.Cog):
    """A command that locks all guild channel"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="lockallvc")
    # @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(administrator=True)
    @commands.cooldown(2, 20, commands.BucketType.guild)
    async def _lockallvc(self, ctx):
        for vc in ctx.guild.voice_channels:
            try:
                await vc.set_permissions(ctx.guild.default_role, connect=False)
            except:
                pass
        vcc = len(ctx.guild.voice_channels)
        embed = Embed(
            title="Locked",
            description=f"Locked **{vcc}** Voice Channels",
            color=discord.Color.blue(),
        )
        await ctx.send(embed=embed)

    @_lockallvc.error
    async def lock_all_vc(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont/'t have permission - `Administrator`")
        if isinstance(error, commands.CheckAnyFailure):
            with open(Path.SettingsPath(), "r") as x:
                settings = load(x)
            await ctx.send(embed=Embed(description=settings["toprolerror"]))


def setup(bot):
    bot.add_cog(LockAllVc(bot))
