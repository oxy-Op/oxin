from extras.directory import Path
from discord.ext import commands 
from discord.embeds import Embed 
from json import load 
from extras.permissions import *

class Lists(commands.Cog):
    """Shows Some Important Information such as server admins etc..."""

    def __init__(self,bot):
        self.bot = bot 

    @commands.command(name='list')
    @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(administrator=True)
    @commands.cooldown(5,10,commands.BucketType.user)
    async def _list(self,ctx,action=None,mode=None):
            if mode and action is not None:
                if action == 'member':
                    if mode == 'bots':
                        bots = ''
                        for member in ctx.guild.members:
                            if member.bot:
                                bots += member.mention + "\n"
                        await ctx.send(embed=Embed(title='Server Bots',description=bots,color=0xea4ce3))
                    elif mode == 'admins':
                        admins = ''
                        for member in ctx.guild.members:
                            if member.guild_permissions.administrator:
                                admins += member.mention + '\n'
                        await ctx.send(embed=Embed(title='Server Admin',description=admins,color=0xfeca32))
                    elif mode == 'bans':
                        bans = ''
                        banlist = await ctx.guild.bans()
                        for member in banlist:
                            bans+= f'**{member.user.name}** - {member.user.id} \n'
                        await ctx.send(embed=Embed(description=bans,color=0xf43e1))
                    else:
                        await ctx.send(embed = Embed(description=':x: No Modes Called `{}` found'.format(mode),color=0xee3ce))
                elif action == 'role':
                    '''if mode == 'bots':
                        bots = ''
                        for role in ctx.guild.roles:
                            if role.is_premium_subscriber:
                                bots += role.mention + ' , '
                            else:
                                return 
                        await ctx.send(embed=Embed(title='Server Bots Roles',description=bots,color=0xffe43c))'''
                    if mode == 'roles':
                        roles = ''
                        for role in ctx.guild.roles:
                            roles+= (role.mention) + ' , '
                        await ctx.send(embed=Embed(title='Server roles',description=roles,color=0xe321ae))
                    elif mode == 'admins':
                        admins = ''
                        for role in ctx.guild.roles:
                            if role.permissions.administrator:
                                admins+= role.mention + '\n'
                        await ctx.send(embed=Embed(title='Admin Roles',description=admins,color=0x3214ec))
                    else:await ctx.send(embed = Embed(description=':x: No Modes Called `{}` found'.format(mode)))
                else:await ctx.send(embed=Embed(description=':x: No Action called : `{}` was found , try using {}help list'.format(action,self.bot.command_prefix)))
            else:
                await ctx.send(embed=Embed(description=':x: Please Provide What type of list you want, List modes can be found using {}help list'.format(self.bot.command_prefix)))
    @_list.error 
    async def err_list(self,ctx,error):
        if isinstance(error,commands.CheckAnyFailure):
            with open(Path.SettingsPath(),'r') as x:
                settings = load(x)
            await ctx.send(
                embed = Embed(description=settings['toprolerror'])
            )
        if isinstance(error,commands.MissingPermissions):
            await ctx.send(embed=Embed(description=':x: You\'re Missing Permission - `Administrator`'))
def setup(bot):
    bot.add_cog(Lists(bot))