from discord import AuditLogAction
from discord.ext import commands
from discord.embeds import Embed
import discord

class MemberBan(commands.Cog):
    """Bot event when a discord server member got banned"""

    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        try:
            async for entry in guild.audit_logs(action=AuditLogAction.ban):
                embed = Embed()
                embed.title = 'Member Banned'
                embed.add_field(name='Member Banned',value=user.name + " - " + str(user.id))
                embed.add_field(name='Banned By ',value=entry.user.mention + "-" + str(entry.user.id))
                embed.add_field(name='Reason',value=entry.reason)
                embed.add_field(name='Server name',value=guild.name)
                embed.add_field(name='At ',value=entry.created_at.strftime('%D:%H:%M:%S'))
                embed.set_footer(text='Banned Logs')
        except commands.BotMissingPermissions:
            pass 


def setup(bot):
    bot.add_cog(MemberBan(bot))