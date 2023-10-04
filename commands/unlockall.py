from extras.permissions import owner, toprole
import discord
from discord.ext import commands
from discord.embeds import Embed
import asyncio
from json import load
from extras.directory import Path


class UnlockAll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unlockall")
    # @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(administrator=True)
    @commands.cooldown(2, 60, commands.BucketType.guild)
    async def _unlockall(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        await ctx.send(
            embed=Embed(
                description="Are You Sure Want to run this command? Type `y` to continue \n NOTE:- This will Unlock all Channels including text and voice \n \nYou have 10 seconds to reply"
            )
        )
        try:
            reply = await self.bot.wait_for("message", check=check, timeout=10)
            if reply.content == "y":
                for channels in ctx.guild.channels:
                    try:
                        await channels.set_permissions(
                            ctx.guild.default_role,
                            send_messages=True,
                            connect=True,
                            view_channel=True,
                            reason=ctx.author.name,
                        )
                        embed = discord.Embed(
                            title="Unlocked all",
                            description=f"Sucessfully Unlocked All Channels \n Admin : {ctx.author.mention} \n \n",
                        )
                        embed.set_footer(
                            text=f"Unlocked Channels at {ctx.message.created_at}",
                            icon_url=ctx.author.avatar_url,
                        )
                    except:
                        pass
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=Embed(description=":x: Command cancelled"))
        except asyncio.TimeoutError:
            await ctx.send(embed=Embed(description=":x: Timeout"))

    @_unlockall.error
    async def unlockall_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don/'t Have Permission - `Administrator`")
        if isinstance(error, commands.CheckAnyFailure):
            with open(Path.SettingsPath(), "r") as x:
                settings = load(x)
            await ctx.send(embed=Embed(description=settings["toprolerror"]))


def setup(bot):
    bot.add_cog(UnlockAll(bot))
