from json import load
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from extras.directory import Path
from discord.embeds import Embed

class Report(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.command(name='report')
    @commands.cooldown(3,3600,BucketType.user)
    async def _report(self,ctx,*,bug=None):
        if bug is not None:
            with open(Path.SettingsPath(),'r') as b:
                debug = load(b)
            debuggers = debug['debuggers']
            for users in debuggers:
                debugger = await self.bot.fetch_user(users)
                embed = Embed()
                embed.color = 0xffff00
                embed.title = "Bugs Reported in {}".format(ctx.guild.name)
                embed.description = f"-- {bug} --"
                embed.set_footer(text='Bugs reported by {} | ID : {}'.format(ctx.author.name,ctx.author.id))
                try:
                    await debugger.send(embed=embed)
                except Exception as e:
                    print(e, "\n",debugger.name , 'has turned off thier dm')
            await ctx.send(embed=Embed(description='Successfully reported',color=0xeeaabb))
                
        else:
            await ctx.send(f"{ctx.author.mention} , Please Type what you want to report, More Help at {self.bot.command_prefix}help report ")


def setup(bot):
    bot.add_cog(Report(bot))