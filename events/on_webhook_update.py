from discord.ext import commands
from discord.embeds import Embed

class WebookUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_webhooks_update(self,channel):
        embed = Embed()
        embed.description = 'Webhook updated in {}'.format(channel.mention)
        embed.color= 0xaaeeff


def setup(bot):
    bot.add_cog(WebookUpdate(bot))