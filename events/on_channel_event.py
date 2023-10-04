import discord
from discord.ext import commands
from discord.embeds import Embed

class EventChannel(commands.Cog):
    """An Class for discord channel events"""

    def __init__(self, bot):
        self.bot=bot

   
    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel):
        try:
            async for entry in channel.guild.audit_logs(limit=1,action=discord.AuditLogAction.channel_create):
                embed = Embed()
                embed.color = 0xeac431
                embed.title = 'Channel created'
                embed.add_field(name='Name ',value=channel.name)
                embed.add_field(name='ID ',value=channel.id)
                embed.add_field(name='Created by ',value=entry.user.mention)
                embed.add_field(name='Reason ',value=entry.reason)
                embed.add_field(name='Created at ',value=entry.created_at)
        except commands.BotMissingPermissions:
            pass 
        
    @commands.Cog.listener()
    async def on_guild_channel_delete(self,channel):
        try:
            async for entry in channel.guild.audit_logs(limit=1,action=discord.AuditLogAction.channel_delete):
                embed = Embed()
                embed.color = 0xeac431
                embed.title = 'Channel deleted'
                embed.add_field(name='Name ',value=channel.name)
                embed.add_field(name='ID ',value=channel.id)
                embed.add_field(name='deleted by ',value=entry.user.mention)
                embed.add_field(name='Reason ',value=entry.reason)
                embed.add_field(name='deleted at ',value=entry.created_at)
        except commands.BotMissingPermissions:
            pass

    @commands.Cog.listener()
    async def on_guild_channel_update(self,before, after):
        try:
            async for entry in before.guild.audit_logs(limit=1,action=discord.AuditLogAction.channel_update):
                embed = Embed()
                embed.color = 0xf321ea
                embed.title = 'Channel updated'
                embed.description = '{} Updated the channel {} at {}'.format(entry.user.mention,before.name,entry.created_at)
                embed.add_field(name='Before name',value=before.name)
                embed.add_field(name='After name ',value=after.name)
                embed.add_field(name='At ',value=entry.created_at)
        except commands.BotMissingPermissions:
            pass


def setup(bot):
    bot.add_cog(EventChannel(bot))