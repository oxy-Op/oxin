import discord
from discord.ext import commands
from discord.embeds import Embed
from json import load
from extras.directory import Path
from extras.permissions import *


class UnlockAllVc(commands.Cog):
    """A Command that Unlocks all voice channels"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unlockallvc")
    # @commands.check_any(owner(),toprole())
    @commands.cooldown(2, 20, commands.BucketType.guild)
    @commands.has_guild_permissions(administrator=True)
    async def _unlockallvc(self, ctx):
        for vcs in ctx.guild.voice_channels:
            await vcs.set_permissions(ctx.guild.default_role, connect=True)
        vcc = len(ctx.guild.voice_channels)
        embed = Embed(
            title="Unlocked",
            description=f"Unlocked **{vcc}** Voice Channels",
            color=discord.Color.blue(),
        )
        await ctx.send(embed=embed)

    @_unlockallvc.error
    async def _unlock_all_vc(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont/'t have permission - `Administrator`")
        if isinstance(error, commands.CheckAnyFailure):
            with open(Path.SettingsPath(), "r") as x:
                settings = load(x)
            await ctx.send(embed=Embed(description=settings["toprolerror"]))


def setup(bot):
    bot.add_cog(UnlockAllVc(bot))
