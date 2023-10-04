from discord.ext import commands


def toprole():
    def predict(ctx):
        return ctx.author.top_role >= ctx.guild.me.top_role
    return commands.check(predict)

def owner():
    def predicate(ctx):
        return ctx.author.id == ctx.guild.owner.id
    return commands.check(predicate)

