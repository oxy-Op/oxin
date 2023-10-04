from discord.ext import commands

class Error(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    """An Error Handler for commands"""

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send('**This command is on cooldown for %.2fs **' % error.retry_after)
            if isinstance(error,commands.CommandNotFound):
                return
            if isinstance(error,commands.BotMissingPermissions):
                await ctx.send('It Looks Like I Dont have permission to execute this command. Please Check My Role Position and permissions')
            else:
                print(error)

def setup(bot):
    bot.add_cog(Error(bot))