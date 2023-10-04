import discord
from discord.ext import commands
from discord.embeds import Embed
from json import load 
from extras.directory import Path
from extras.permissions import *

class Kick(commands.Cog):
    """Command for kicking member from server \n 
       Parameters : \n `Member`:`discord.Member` \n `Reason`: str (optional)
    """
    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='kick')
    @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(kick_members=True)
    @commands.cooldown(1,2,commands.BucketType.user)
    async def _kick(self,ctx, member: discord.Member, *, reason='Not Provided'):
        if member.top_role < ctx.guild.me.top_role:
            if member in ctx.guild.members:
                await member.kick(reason=f"{ctx.author.name} : {str(reason)}")
                embed = discord.Embed(title='Kicked',description=f':white_check_mark: Successfully Kicked {member.mention} \n Admin : {ctx.author.mention} \n Reason : {reason}',color=0xee45ff)
                await ctx.send(embed=embed)
            else:
                await ctx.send(embed=Embed(description=f':x: **{member.name}** is not in server'))
        else:
            await ctx.send(embed=Embed(description=':x: Please check my role postion'))
    @_kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send(":x: You Don\'t Have Permission - `KICK MEMBERS`")
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(title="Usage - Kick",description=f"To kick a member Run \n{self.bot.command_prefix}kick <member> (reason)")
            await ctx.send(embed=embed)
        if isinstance(error,commands.UserNotFound):
            await ctx.send(embed=Embed(description=':x: Member not found'))
        if isinstance(error,commands.CheckAnyFailure):
            with open(Path.SettingsPath(),'r') as x:
                settings = load(x)
            await ctx.send(
                embed = Embed(description=settings['toprolerror'])
            )
def setup(bot):
    bot.add_cog(Kick(bot))