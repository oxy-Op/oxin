import discord
from discord.ext import commands
from discord.embeds import Embed
import asyncio
from json import load
from extras.directory import Path
from extras.permissions import *


class LockAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="lockall", aliases=["lockallchannel"])
    # @commands.check_any(owner(),toprole())
    @commands.cooldown(2, 60, commands.BucketType.guild)
    @commands.has_guild_permissions(administrator=True)
    async def _lockall(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send(
            embed=Embed(
                description="Are You Sure Want to run this command? \n Type `y` to continue \n NOTE:- This will lock all Channels including text and voice \n \nYou have 10 seconds to reply",
                color=0xFEFEAF,
            )
        )
        try:
            reply = await self.bot.wait_for("message", check=check, timeout=10)
            if reply.content == "y":
                for channels in ctx.guild.channels:
                    try:
                        await channels.set_permissions(
                            ctx.guild.default_role,
                            send_messages=False,
                            connect=False,
                            reason=ctx.author.name,
                        )
                    except:
                        pass
                embed = discord.Embed(
                    title="Locked all",
                    description=f"Sucessfully Locked All Channels \n Admin : {ctx.author.mention} \n \n",
                    color=0xDEDEDE,
                )
                embed.set_footer(
                    text=f"Locked Channels at {ctx.message.created_at}",
                    icon_url=ctx.author.avatar_url,
                )
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=Embed(description=":x: Command cancelled"))
        except asyncio.TimeoutError:
            await ctx.send(embed=Embed(description=":x: Timeout"))

    @_lockall.error
    async def lockall_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don/'t Have Permission - `Administrator`")
        if isinstance(error, commands.CheckAnyFailure):
            with open(Path.SettingsPath(), "r") as x:
                settings = load(x)
            await ctx.send(embed=Embed(description=settings["toprolerror"]))


def setup(bot):
    bot.add_cog(LockAll(bot))
