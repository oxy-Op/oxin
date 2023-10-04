from extras.permissions import owner, toprole
import discord
from discord.ext import commands
from discord.embeds import Embed
from json import load
import asyncio
from extras.directory import Path

class Maintainance(commands.Cog):
    """Command that does lockallchannel and creates a channel named maintainance \n
    parameters: \n
    `mode`: <on | off>
    """

    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='maintainance')
    # @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(administrator=True)
    @commands.cooldown(2,40,commands.BucketType.guild)
    async def _maintainance(self,ctx,mode):
            if mode == str('on'):
                def check(m):
                    return m.author == ctx.author and m.channel == ctx.channel
                emb = discord.Embed(title='Lock All Channels?',description='Do you want to deny view channel permission from everyone? \nReply in `y` to proceed',color=0xff0000)
                emb.set_footer(text='You have 10 seconds to reply')
                ms = await ctx.send(embed=emb)
                try:
                    reply = await self.bot.wait_for('message',check=check,timeout=10)
                    if reply.content == str('y'):
                        emb0 = discord.Embed()
                        emb0.description = 'Proceeding...'
                        msg = await ctx.send(embed=emb0)
                        await asyncio.sleep(2)
                        emb0.description = ':white_check_mark: Proceeded \nFetching guild channels...'
                        await msg.edit(embed=emb0)
                        emb0.description = ':white_check_mark: Proceeded \n:white_check_mark:Successfully Fetched guild channels \nOverriding permissions for all channels...'
                        await msg.edit(embed=emb0)
                        for channels in ctx.guild.channels:
                            try:
                                await channels.set_permissions(ctx.guild.default_role,view_channel=False,reason=ctx.author.name)
                            except:
                                pass
                        channel = await ctx.guild.create_text_channel('maintainance chat')
                        emb0.description = ':white_check_mark: Proceeded \n:white_check_mark:Successfully Fetched guild channels \n:white_check_mark:Successfully Overrided permissions for all channels'
                        await msg.edit(embed=emb0)
                        embed = discord.Embed(title="Maintainance Mode", description=f"Successfully Locked All Channels", color=0xff0000)        
                        await ctx.send(embed=embed)
                    else:
                        emb01 = discord.Embed(description=':x: Command cancelled')
                        emb.description='Timeout'
                        await ms.edit(embed=emb)
                        await ctx.send(embed=emb01)
                except asyncio.TimeoutError:
                    await ctx.send(embed=discord.Embed(description=':x: Timeout'),delete_after=3)
                except:
                    pass
            elif mode == str('off'):
                def check(m):
                    return m.author == ctx.author and m.channel == ctx.channel
                emb = discord.Embed(title='Lock All Channels?',description='Do you want to deny view channel permission from everyone? \nReply in `y` to proceed',color=0xff0000)
                emb.set_footer(text='You have 10 seconds to reply')
                ms = await ctx.send(embed=emb)
                try:
                    reply = await self.bot.wait_for('message',check=check,timeout=10)
                    if reply.content == str('y'):
                        emb0 = discord.Embed()
                        emb0.description = 'Proceeding...'
                        msg = await ctx.send(embed=emb0)
                        await asyncio.sleep(2)
                        emb0.description = ':white_check_mark: Proceeded \nFetching guild channels...'
                        await msg.edit(embed=emb0)
                        emb0.description = ':white_check_mark: Proceeded \n:white_check_mark:Successfully Fetched guild channels \nOverriding permissions for all channels...'
                        await msg.edit(embed=emb0)
                        for channels in ctx.guild.channels:
                            try:
                                await channels.set_permissions(ctx.guild.default_role,view_channel=True,reason=ctx.author.name)
                            except:
                                pass
                        emb0.description = ':white_check_mark: Proceeded \n:white_check_mark:Successfully Fetched guild channels \n:white_check_mark:Successfully Overrided permissions for all channels'
                        await msg.edit(embed=emb0)
                        embed = discord.Embed(title="Maintainance Mode", description=f"Successfully Unlocked All Channels", color=0xff0000)        
                        await ctx.send(embed=embed)
                    else:
                        emb01 = discord.Embed(description=':x: Command cancelled')
                        await ctx.send(embed=emb01)
                except asyncio.TimeoutError:
                    await ctx.send(embed=Embed(description=':x: Timeout'),delete_after=4)
                
    

    @_maintainance.error
    async def error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send(embed=Embed(description=':x: Missing Argument `mode` \n Example:- `{}maintainance on | off`'.format(self.bot.command_prefix)))
        if isinstance(error,commands.MissingPermissions):
                await ctx.send("You dont/'t have permission - `Administrator`")
        if isinstance(error,commands.CheckAnyFailure):
            with open(Path.SettingsPath(),'r') as x:
                settings = load(x)
            await ctx.send(
                embed = Embed(description=settings['toprolerror'])
            )


def setup(bot):
    bot.add_cog(Maintainance(bot))