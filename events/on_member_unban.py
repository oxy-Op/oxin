from discord import AuditLogAction
from discord.ext import commands
from discord.embeds import Embed 

class MemberUnban(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_member_unban(self, guild, user):
        try:
            async for entry in guild.audit_logs(action=AuditLogAction.unban,limit=1):
                embed = Embed()
                embed.title = 'Member Unbanned'
                embed.add_field(name='Member Unbanned',value=user.name + " - " + str(user.id))
                embed.add_field(name='Unbanned By ',value=entry.user.mention + "-" + str(entry.user.id))
                embed.add_field(name='Reason',value=entry.reason)
                embed.add_field(name='Server name',value=guild.name)
                embed.add_field(name='At ',value=entry.created_at.strftime('%D:%H:%M:%S'))
        except commands.BotMissingPermissions:
            pass


def setup(bot):
    bot.add_cog(MemberUnban(bot))