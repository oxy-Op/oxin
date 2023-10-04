import discord
from discord.ext import commands
from discord.embeds import Embed 
import asyncio

class Help(commands.Cog):
    """Help command for bot"""

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='help',aliases=['h','commands'])
    async def _help(self,ctx,command=None):
        if command is None:
            embed = discord.Embed(description=f'Use command name after help to get more information about the command - `{self.bot.command_prefix}help info`',color=0xff004c)
            embed.set_thumbnail(url=self.bot.user.avatar_url)
            embed.add_field(
            name='**Normal commands \n**',value=f'`help` `invite` \n `userinfo` `serverinfo` \n `info`',inline=False
            )
            embed.add_field(name='**Admin commands**',value=' `clear` `kick` `ban` \n `mute` `unmute` `unban` \n `lock` `unlock` \n `lockall` `lockallvc` `unbanall` \n `unlockall` `unlockallvc` **`maintainance`**',inline=False)
            embed.add_field(name='Anti Nuke',value='`list`',inline=False)
            embed.add_field(name='Utility',value ='`ping` `report`',inline=False)
            await ctx.send(embed=embed)
        elif command == 'help':
            embed = Embed(description='\n \n `{}help` - **Shows a list of commands of bot** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg = await ctx.send(embed=embed)
            await msg.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction and user:
                    await msg.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'invite':
            embed = Embed()
            embed = Embed(description='\n \n `{}invite` - **Sends an invitation link of bot** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'userinfo':
            embed = Embed()
            embed = Embed(description='\n \n `{}userinfo <User | ID>` - **Shows Information about user** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'serverinfo':
            embed = Embed()
            embed = Embed(description='\n \n `{}serverinfo` - **Shows Information about current server** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'info':
            embed = Embed()
            embed = Embed(description='\n \n `{}info` - **Shows Information about bot** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'clear':
            embed = Embed()
            embed = Embed(description='\n \n `{}clear <amount>` - **Purge messages in current channel \n Amount Must be above 0 and below 100000** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'kick':
            embed = Embed()
            embed = Embed(description='\n \n `{}kick <User | ID> (reason)` - **kicks a member \n Must Mention User/ID. \n Reason is optional** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'ban':
            embed = Embed()
            embed = Embed(description='\n \n `{}ban <User | ID> (reason)` - **ban a member \n Must Mention User/ID. \n Reason is optional** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'lock':
            embed = Embed()
            embed = Embed(description='\n \n `{}lock <Channel | ID> (reason)` - **Locks a channel \n Must Mention Chaanel/ID. \n Reason is optional** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'unlock':
            embed = Embed()
            embed = Embed(description='\n \n `{}unlock <Channel | ID> (reason)` - **Unlocks a channel \n Must Mention Chaanel/ID. \n Reason is optional** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'mute':
            embed = Embed()
            embed = Embed(description='\n \n `{}mute <User | ID> (reason)` - **mutes a member \n Must Mention User/ID. \n Reason is optional** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'unmute':
            embed = Embed()
            embed = Embed(description='\n \n `{}unmute <User | ID> (reason)` - **unmute a member \n Must Mention User/ID. \n Reason is optional** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'unban':
            embed = Embed()
            embed = Embed(description='\n \n `{}unban <User | ID> (reason)` - **unban an user \n Must Mention User/ID. \n Reason is optional** \n \n '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'lockall':
            embed = Embed()
            embed = Embed(description='\n \n `{}lockall` - **Locks all channels in a server** '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'lockallvc':
            embed = Embed()
            embed = Embed(description='\n \n `{}lockallvc` - **locks all voice channels** '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'unlockallvc':
            embed = Embed()
            embed = Embed(description='\n \n `{}unlockallvc` - **unlocks all voice channels** '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'unbanall':
            embed = Embed()
            embed = Embed(description='\n \n `{}unbanall` - **Unban all Banned Members** '.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'unlockall':
            embed = Embed()
            embed = Embed(description='\n \n `{}unlockall` - **unlocks all channels of server**'.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'maintainance':
            embed = Embed()
            embed = Embed(description='\n \n `{}maintainance < on | off >` - **When Set to `on` Deny View channel permission for everyone and creates a channel \n When set to `off` Unlocks View Channel Permission for everyone **'.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'list':
            embed = Embed()
            embed = Embed(description='`{0}list <action> <mode>` - **This command helps you to get information about what is happening in your server \n Example:- `{0}list member bots` - list all bots \n Usage:- Currently there are these lists :\n \n `{0}list member bots \n{0}list member admins \n{0}list member bans` \n \n `{0}list role roles \n{0}list role admins` \n **'.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'ping':
            embed = Embed()
            embed = Embed(description='`{0}ping` - **Shows bot latency**'.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass
        elif command == 'report':
            embed = Embed()
            embed = Embed(description='`{0}report <bug>` - **Reports bug and sends to bot developers \n NOTE:- You might get rate-limited and command go for cooldown**'.format(self.bot.command_prefix),color=0xff3e4c)
            msg2 = await ctx.send(embed=embed)
            await msg2.add_reaction('🗑')
            def check(reaction, user):
                return user == ctx.author and str(reaction.emoji) == '🗑'
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                if reaction.message == msg2:
                    await msg2.delete()
            except asyncio.TimeoutError:
                pass

def setup(bot):
    bot.add_cog(Help(bot))