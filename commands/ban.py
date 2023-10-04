import discord
from discord.ext import commands
from discord.embeds import Embed 
import requests 
from json import load
from extras.directory import Path
from extras.permissions import owner , toprole

class Ban(commands.Cog):
    def __init__(self, bot, token):
        self.bot=bot
        self._token = token


    @commands.command(name='ban')
    @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(administrator=True)
    @commands.cooldown(1,2,commands.BucketType.user)
    async def _ban(self,ctx,member:discord.Member,*,reason="Not Provided"):
        if ctx.guild.me.top_role > member.top_role:
            request = requests.Session()
            headers = {
            'authorization':'Bot ' + self._token
            }
            json= {
            'reason':f"{ctx.author.name} : {str(reason)}"
            }
            r = request.put(f'https://canary.discord.com/api/v8/guilds/{ctx.guild.id}/bans/{member.id}',headers=headers,json=json)
            if r.status_code == 204:
                embed = discord.Embed(title="Banned",description=f":white_check_mark: Successfully Banned {member.mention} \n Admin : {ctx.author.mention} \n Reason : {str(reason)} ")
                await ctx.send(embed=embed)
        else:
            await ctx.send(embed=Embed(description=':x: Please Check My Role Position',color=0xfeafef))
    

    @_ban.error
    async def ban_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send(":x: You Don\'t Have Permission - `BAN MEMBERS`")
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(title="Usage - ban",description=f"To ban a member Run \n{self.bot.command_prefix}ban <member> (reason)")
            await ctx.send(embed=embed)
        if isinstance(error,commands.MemberNotFound):
            await ctx.send(embed=Embed(description=':x: Member not found'))
        if isinstance(error,commands.CheckAnyFailure):
            with open(Path.SettingsPath(),'r') as x:
                settings = load(x)
            await ctx.send(
                embed = Embed(description=settings['toprolerror'])
            )


def setup(bot):
    bot.add_cog(Ban(bot))