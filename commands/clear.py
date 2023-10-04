import discord
from discord.ext import commands
from discord.embeds import Embed
from json import load
from extras.directory import Path
from extras.permissions import *

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='clear',aliases=['purge'])
    @commands.check_any(owner(),toprole())
    @commands.has_permissions(manage_messages=True,read_message_history=True)
    @commands.cooldown(3,1,commands.BucketType.user)
    async def _clear(self,ctx,amount: int):
            await ctx.message.delete()
            try:
                if amount <= 0:
                    await ctx.send(embed=Embed(description=f":x: Please Choose Amount Above **0**"))
                elif amount >= 100000:
                    await ctx.send(embed=Embed(description=f":x: Please Choose Amount Below **100000**"))
                else:
                    channel = ctx.channel
                    messages = []
                    async for message in channel.history(limit=amount):
                        messages.append(message)
                    await channel.purge(limit=len(messages))
                    embed = discord.Embed(title="Purged",description=f"Purged **{len(messages)}** Messages \nModerator : {ctx.author.mention} ",color=discord.Color.green())
                    await ctx.send(embed=embed)
            except Exception as e:
                print(e)
        

    @_clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send(embed=Embed(description=f"You are missing permissions - `Manage Messages` Read_Message_History`"))
        if isinstance(error,commands.MissingRequiredArgument):
            embed = discord.Embed(title="Purge",description= f"To Purge Run \n {self.bot.command_prefix}purge <amount> \n \n ",color=discord.Color.blue())
            await ctx.send(embed=embed)
        if isinstance(error,commands.CheckAnyFailure):
            with open(Path.SettingsPath(),'r') as x:
                settings = load(x)
            await ctx.send(
                embed = Embed(description=settings['toprolerror'])
            )



def setup(bot):
    bot.add_cog(Clear(bot))