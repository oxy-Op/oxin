from json import load
from extras.directory import Path
from discord.ext import commands
from discord.embeds import Embed
from extras.database import *
from extras.permissions import *

class Config(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='config',aliases=['configurations'])
    @commands.has_guild_permissions(administrator=True)
    async def _config(self,ctx):
            embed1 = Embed()
            embed1.color = 0xe8cb2a
            embed1.title = 'Server Configurations'
            embed1.add_field(name='[1] Bans and Unban Logs',value=None,inline=False)
            embed1.add_field(name='[2] Role Regarding Logs',value=None,inline=False)
            embed1.add_field(name='[3] Channel Regarding Logs',value=None,inline=False)
            embed1.add_field(name='[4] Webhook Regarding Logs',value=None,inline=False)
            embed1.add_field(name='[5] Message deleted logs',value=None,inline=False)
            embed1.add_field(name='[6] Message edited Logs',value=None,inline=False)
            embed1.add_field(name='[0] All logs <DM | CHANNEL>',value=None,inline=False)
            embed1.add_field(name='What is DM? ',value='It will set all logs or specific logs to users dm, After that They will ask to accept by typing `y` in dm, Must Provide user id , Limited 5 users'.capitalize())
            embed1.set_footer(text='Use {0}logs add <logsID> <channel> to add | {0}logs remove <logsID>'.format(self.bot.command_prefix))
            await ctx.send(embed=embed1)
    
    @_config.error 
    async def c_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You're Missing Permissions - `Administrator`")
        if isinstance(error,commands.CheckAnyFailure):
            with open(Path.SettingsPath(),'r') as x:
                settings = load(x)
            await ctx.send(
                embed = Embed(description=settings['toprolerror'])
            )


def setup(bot):
    bot.add_cog(Config(bot))