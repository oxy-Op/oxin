from json import load
from discord.embeds import Embed
from extras.directory import Path
from discord.ext import commands
from extras.permissions import owner, toprole
from extras.database import *
from sqlite3 import OperationalError


class Logs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="log")
    # @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(administrator=True)
    @commands.bot_has_guild_permissions(view_audit_log=True)
    async def _log(self, ctx, log=None, mode=None, id=None):
        with open(Path.SettingsPath(), "r") as q:
            settings = load(q)
        if log in settings["logsID"]:
            if id is not None:
                if mode == "channel":
                    try:
                        execute(
                            f"""INSERT INTO SaveServerChannels (ServerID,LogChannel,LogID,UserRegistered)
                            VALUES ({ctx.guild.id},{id},{log},'{ctx.author.name}')
                            """
                        )
                    except OperationalError:
                        execute(
                            f"""UPDATE SaveServerChannels SET LogChannel = {id}, LogID = {log}, UserRegistered = {ctx.author.name} WHERE ServerID = {ctx.guild.id} """
                        )

            else:
                await ctx.send(
                    embed=Embed(
                        description=":x: Please Type ID | Example : {}log channel 1 1234567890123 ".format(
                            self.bot.command_prefix
                        )
                    )
                )
        else:
            await ctx.send(
                embed=Embed(
                    description="Log ID not provided, Please consider {}config for more information".format(
                        self.bot.command_prefix
                    )
                )
            )

        9

    @_log.error
    async def log_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You are missing permission - `Administrator`")
        if isinstance(error, commands.CheckAnyFailure):
            with open(Path.SettingsPath(), "r") as x:
                settings = load(x)
            await ctx.send(embed=Embed(description=settings["toprolerror"]))


def setup(bot):
    bot.add_cog(Logs(bot))
