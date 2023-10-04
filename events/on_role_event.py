import discord
from discord.ext import commands
from discord.embeds import Embed


class EventRole(commands.Cog):
    """An Class for discord role events"""

    def __init__(self, bot):
        self.bot=bot


    @commands.Cog.listener()
    async def on_guild_role_create(self,role):
        try:
            async for entry in role.guild.audit_logs(limit=1,action=discord.AuditLogAction.role_create):
                embed = Embed()
                embed.color = 0xffffff
                embed.title = 'Role Created'
                embed.add_field(name='Role created ',value=entry.target)
                embed.add_field(name='Created by ',value=entry.user.mention + ' - ' + str(entry.user.id))
                embed.add_field(name='Reason',value=entry.reason)
                embed.add_field(name='At ',value=entry.created_at.strftime('%D:%H:%M:%S'))
        except commands.BotMissingPermissions:
            pass

    @commands.Cog.listener()
    async def on_guild_role_delete(self,role):
        try:
            async for entry in role.guild.audit_logs(limit=1,action=discord.AuditLogAction.role_delete):
                embed = Embed()
                embed.color = 0xffffff
                embed.title = 'Role Deleted'
                embed.add_field(name='Role Deleted ',value=role.name)
                embed.add_field(name='Deleted by ',value=entry.user.mention + ' - ' + str(entry.user.id))
                embed.add_field(name='Reason',value=entry.reason)
                embed.add_field(name='At ',value=entry.created_at.strftime('%D:%H:%M:%S'))
        except commands.BotMissingPermissions:
            pass

    @commands.Cog.listener()
    async def on_guild_role_update(self,before, after):
        try:
            async for entry in before.guild.audit_logs(limit=1,action=discord.AuditLogAction.role_update):
                embed = Embed()
                embed.title ='Role updated'
                embed.color = 0xfeacea
                embed.description = '{} updated the role {} at {}'.format(entry.user.mention,before.name,entry.created_at)
                embed.add_field(name='Before name',value=before.name)
                embed.add_field(name='After name',value=after.name)
                embed.add_field(name='Before color',value=before.color)
                embed.add_field(name='After color',value=after.color)
                embed.add_field(name='Before hoist',value=before.hoist)
                embed.add_field(name='After hoist',value=after.hoist)
                embed.add_field(name='Position changed',value=True if before.position != after.position else False)
                embed.add_field(name='Permission changed',value=True if before.permissions != after.permissions else False)
        except commands.BotMissingPermissions:
            pass


def setup(bot):
    bot.add_cog(EventRole(bot))