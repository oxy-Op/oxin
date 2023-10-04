from discord.ext import commands 
from discord.embeds import Embed
from discord import __version__

class Info(commands.Cog):
    """An Info command for bot"""

    def __init__(self,bot):
        self.bot = bot 

    @commands.command(name='info',aliases=['about','botinfo'])
    async def _info(self,ctx):
        owner = await self.bot.fetch_user(728893914714603580)
        contro = await self.bot.fetch_user(704224143402598472)
        embed = Embed(title='Information about bot',color=0x55eeff)
        embed.add_field(name='Name',value=self.bot.user.name)
        embed.add_field(name='ID',value=self.bot.user.id)
        embed.add_field(name='Version',value='0.1')
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name='Owner',value=owner.name)
        embed.add_field(name='Programmer',value=owner.name)
        embed.add_field(name='Contributors',value=contro.name)
        embed.add_field(name='Programming Language',value='Python | Version: 3.8.10')
        embed.add_field(name='API Wrapper',value='discord {}'.format(__version__))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))