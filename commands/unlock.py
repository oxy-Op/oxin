import discord
from discord.ext import commands
from discord.embeds import Embed
from json import load
from extras.directory import Path
from extras.permissions import *


class Unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unlock")
    # @commands.check_any(owner(),toprole())
    @commands.has_permissions(administrator=True)
    @commands.cooldown(3, 5, commands.BucketType.channel)
    async def _unlock(
        self, ctx, channel: discord.TextChannel, *, reason="Not Provided"
    ):
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        if overwrite.send_messages == True:
            await ctx.send(
                embed=Embed(
                    description=":x: Channel is already unlocked", color=0xFFFF00
                )
            )
        else:
            await channel.set_permissions(
                ctx.guild.default_role,
                send_messages=True,
                reason=f"{ctx.author.name} : {str(reason)}",
            )
            embed = discord.Embed(
                title="Unlocked Channel",
                description=f"Unlocked {channel.mention} \n Moderator : {ctx.author.mention} \nReason : {str(reason)}",
                color=0xFFEEAA,
            )
            await ctx.send(embed=embed)

    @_unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont/'t have permission - `Administrator`")
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title="Usage - Unlock channel",
                description=f"{self.bot.command_prefix}unlock <#channel | ID> (reason)",
            )
            await ctx.send(embed=embed)
        if isinstance(error, commands.CheckAnyFailure):
            with open(Path.SettingsPath(), "r") as x:
                settings = load(x)
            await ctx.send(embed=Embed(description=settings["toprolerror"]))


def setup(bot):
    bot.add_cog(Unlock(bot))
