import discord
from discord.ext import commands
import asyncio
from discord.embeds import Embed
from json import load
from extras.directory import Path
from extras.permissions import *

class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='unmute')
    # @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(manage_roles=True)
    @commands.cooldown(2,2,commands.BucketType.user)
    async def _unmute(self,ctx,member:discord.Member,*,reason="Not Provided"):
            await ctx.message.delete()
            try:
                guild = ctx.guild
                Role = discord.utils.get(guild.roles,name="Muted")
                if not Role:
                    message = await ctx.send(':x: Muted role not found')
                    mutedRole = await guild.create_role(name="Muted")
                    await asyncio.sleep(2)
                    await message.edit(content=" Setting Up Muterole...")
                    for channel in guild.channels:
                        await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False) 
                    await message.edit(content=":white_check_mark: Success \n Fetching role...")
                    await asyncio.sleep(1)
                    await message.edit(content=":white_check_mark: Success \n:white_check_mark: Fetched role \n Overriding Permissions for Text channels...")
                    await asyncio.sleep(1)
                    await message.edit(content=":white_check_mark: Success \n:white_check_mark: Fetched role \n :white_check_mark:Overrided Permissions for Text channels \n Overriding Permissions for Voice Channels...")
                    await asyncio.sleep(1)
                    await message.edit(content=":white_check_mark: Success \n:white_check_mark: Fetched role \n:white_check_mark: Overrided Permissions for Text channels \n:white_check_mark: Overrided Permissions for Voice Channels \n Overriding Permissions for Categories...")
                    await asyncio.sleep(1)
                    await message.edit(content=":white_check_mark: Success\n:white_check_mark: Fetched role \n:white_check_mark: Overrided Permissions for Text channels \n :white_check_mark:Overrided Permissions for Voice Channels \n:white_check_mark: Overrided Permissions for Categories \n Checking Guild Configurations...")
                    await asyncio.sleep(1)
                    await message.edit(content=":white_check_mark: Success \n:white_check_mark: Fetched role \n:white_check_mark: Overriding Permissions for Text channels \n:white_check_mark: Overrided Permissions for Voice Channels \n:white_check_mark: Overrided Permissions for Categories \n:white_check_mark: Checked Guild Configurations \n \n Setup Completed!")
                else:
                            await member.remove_roles(Role,reason=f"{ctx.author.name} : {str(reason)}")
                            emved = discord.Embed(title="Unmuted", description=f"{member.mention} Successfully Unmuted \n **Unmuted By** {ctx.author.mention} \n Reason : **{str(reason)}**",color= discord.Color.red())
                            await ctx.send(embed=emved)
                            try:
                                memberdm = discord.Embed(title="Unmuted",description= f"You have been Unmuted from {guild.name} \n Unmuted By {ctx.author.name}#{ctx.author.discriminator} \n Reason : {str(reason)}")
                                memberdm.set_footer(text=f"{self.bot.user.name}")
                                await member.send(embed = memberdm)
                            except:
                                pass
    
            except Exception as e:
                print(e)

    @_unmute.error
    async def unmute_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send(f"You're Missing Permission - Manage Roles")
        elif isinstance(error,commands.MissingRequiredArgument):
            emed = discord.Embed(title="Usage - Unmute", description=f"To Unmute Type \n {self.bot.command_prefix}unmute <member> (reason) \n \n",color=discord.Color.purple())
            emed.set_footer(text="Development")
            await ctx.send(embed=emed, delete_after=5)
        elif isinstance(error,commands.MemberNotFound):
            await ctx.send(embed=Embed(description=f':x: Member Not Found'))
        elif isinstance(error,commands.CheckAnyFailure):
            with open(Path.SettingsPath(),'r') as x:
                settings = load(x)
            await ctx.send(
                embed = Embed(description=settings['toprolerror'])
            )



def setup(bot):
    bot.add_cog(Unmute(bot))