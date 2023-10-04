from .on_ready import *
from .on_command_error import *
from .on_message import *
from .on_member_ban import *
from .on_member_unban import *
from .on_role_event import *
from .on_channel_event import *


async def setup(bot):
    await bot.add_cog(Ready(bot))
    await bot.add_cog(Error(bot))
    await bot.add_cog(Message(bot))
    await bot.add_cog(MemberBan(bot))
    await bot.add_cog(MemberUnban(bot))
    await bot.add_cog(EventRole(bot))
    await bot.add_cog(EventChannel(bot))
