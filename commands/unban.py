import discord
from discord.ext import commands
from discord.embeds import Embed
import requests
from json import load 
from extras.directory import Path
from extras.permissions import *

class Unban(commands.Cog):
    def __init__(self, bot,token):
        self.bot=bot
        self._token = token


    @commands.command(name='unban')
    # @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(ban_members=True)
    @commands.cooldown(1,2,commands.BucketType.user)
    async def _unban(self,ctx,user:discord.User,*,reason='Not Provided'):
            request = requests.Session()
            headers = {
            'authorization': 'Bot ' + self._token
            }
            json = {
            'reason': f"{ctx.author.name} : {str(reason)}"
            }
            r = request.delete(f'https://canary.discord.com/api/v8/guilds/{ctx.guild.id}/bans/{user.id}',headers=headers,json=json)
            if r.status_code == 404:
                await ctx.send(embed=Embed(description=f':x: **{user.name}** is not banned'))
            elif r.status_code == 204:
                await ctx.send(embed=Embed(description=':white_check_mark:Successfully Unbanned **{}** '.format(user.name),color=0xaaaeee))
      

    @_unban.error
    async def unban_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send(":x: You Don\'t Have Permission - `BAN MEMBERS`")
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(title="Usage - unban",description=f"To unban a member Run \n{self.bot.command_self.prefix}unban <member> (reason)")
            await ctx.send(embed=embed)
        if isinstance(error,commands.UserNotFound):
            await ctx.send(embed=Embed(description=':x: User not found'))
        if isinstance(error,commands.CheckAnyFailure):
            with open(Path.SettingsPath(),'r') as x:
                settings = load(x)
            await ctx.send(
                embed = Embed(description=settings['toprolerror'])
            )


def setup(bot):
    bot.add_cog(Unban(bot))