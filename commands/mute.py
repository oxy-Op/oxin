import discord
from discord.ext import commands
from discord.embeds import Embed 
from json import load
import asyncio
from extras.directory import Path
from extras.permissions import *


class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='mute')
    # @commands.check_any(owner(),toprole())
    @commands.has_guild_permissions(manage_roles=True)
    @commands.cooldown(2,2,commands.BucketType.user)
    async def _mute(self,ctx,member:discord.Member,*,reason="Not Provided"):
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
                await member.add_roles(Role,reason=f"{ctx.author.name} {str(reason)}")
                emved = discord.Embed(title="Muted", description=f"{member.mention} Successfully Muted \n **Muted By** {ctx.author.mention} \n Reason : **{str(reason)}**",color= discord.Color.red())
                await ctx.send(embed=emved)
                membed = discord.Embed(title="Muted",description= f"You have been muted from {guild.name} \n Muted By {ctx.author.name}#{ctx.author.discriminator} \n Reason : {str(reason)}")
                membed.set_footer(text=f"{self.bot.user.name}")
                try:
                    await member.send(embed = membed)     
                except:
                    pass
        
    @_mute.error
    async def mute_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send(f"You /'re Missing Permission - Manage Roles")
        if isinstance(error,commands.MissingRequiredArgument):
            emed = discord.Embed(title="Usage - Mute", description=f"To Mute Type \n {self.bot.command_prefix}mute <member> (reason) \n \n",color=discord.Color.purple())
            emed.set_footer(text="Development")
            await ctx.send(embed=emed, delete_after=5)
        if isinstance(error,commands.CheckAnyFailure):
            with open(Path.SettingsPath(),'r') as x:
                settings = load(x)
            await ctx.send(
                embed = Embed(description=settings['toprolerror'])
            )


def setup(bot):
    bot.add_cog(Mute(bot))