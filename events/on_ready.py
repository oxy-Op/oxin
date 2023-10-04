import discord
from discord.ext import commands , tasks
from itertools import cycle

activities = cycle(["Prefix: o! | Listening o!help","https://github.com/oxy-Op","Your server is secured"])

class Ready(commands.Cog):
    """Shows that bot is ready and change status of bot"""

    def __init__(self, bot):
        self.bot = bot
        self.status.start()
        
        
    @tasks.loop(seconds=60)
    async def status(self):
        await self.bot.wait_until_ready()
        await self.bot.change_presence(activity=discord.Game(name=next(activities)),status=discord.Status.do_not_disturb,afk=False)

    @commands.Cog.listener()
    async def on_ready(self):
        for key in self.bot.all_commands:
            print(
                '''Command Loaded : {}'''.format(key)
            )
        print(
            '''Bot is online \nName: {} \nID: {} \nServers : {} \nCommands: {} Including aliases'''.format(self.bot.user.name,self.bot.user.id,len(self.bot.guilds),len(self.bot.all_commands))
        )


def setup(bot):
    bot.add_cog(Ready(bot))