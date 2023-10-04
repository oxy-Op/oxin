import discord
from discord.ext import commands
import asyncio
from discord.embeds import Embed
from json import load
from extras.directory import Path
from extras.permissions import *


class UnbanAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unbanall")
    # @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(administrator=True)
    @commands.cooldown(1, 30, commands.BucketType.guild)
    async def _unbanall(self, ctx):
        banlist = await ctx.guild.bans()
        for users in banlist:
            try:
                await asyncio.sleep(2)
                await ctx.guild.unban(user=users.user)
            except:
                pass
        users = len(banlist)
        embed = Embed(
            title="Unban",
            description=f":white_check_mark:Successfully Unbanned {users} User(s)",
            color=discord.Color.blue(),
        )
        await ctx.send(embed=embed)

    @_unbanall.error
    async def unbanall_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don/'t Have Permission - `Administrator`")
        if isinstance(error, commands.CheckAnyFailure):
            with open(Path.SettingsPath(), "r") as x:
                settings = load(x)
            await ctx.send(embed=Embed(description=settings["toprolerror"]))


def setup(bot):
    bot.add_cog(UnbanAll(bot))
