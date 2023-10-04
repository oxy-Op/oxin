from extras.credentials import Credentials
from .ban import *
from .clear import *
from .help import *
from .info import *
from .invite import *
from .kick import *
from .list import *
from .unlock import *
from .lockall import *
from .lockallvc import *
from .maintainance import *
from .mute import *
from .server import *
from .unban import *
from .unbanall import *
from .unlockall import *
from .unlockallvc import *
from .unmute import *
from .userinfo import *
from .config import *
from .lock import *
from .ping import *
from .report import *
from .logs import *


def setup(bot):
    TOKEN = Credentials._token()
    bot.add_cog(Ban(bot, TOKEN))
    bot.add_cog(Clear(bot))
    bot.add_cog(Help(bot))
    bot.add_cog(Info(bot))
    bot.add_cog(Invite(bot))
    bot.add_cog(Kick(bot))
    bot.add_cog(Lists(bot))
    bot.add_cog(Unlock(bot))
    bot.add_cog(LockAll(bot))
    bot.add_cog(LockAllVc(bot))
    bot.add_cog(Maintainance(bot))
    bot.add_cog(Mute(bot))
    bot.add_cog(ServerInfo(bot))
    bot.add_cog(Unban(bot, TOKEN))
    bot.add_cog(UnbanAll(bot))
    bot.add_cog(UnlockAll(bot))
    bot.add_cog(UnlockAllVc(bot))
    bot.add_cog(Unmute(bot))
    bot.add_cog(UserInfo(bot))
    bot.add_cog(Config(bot))
    bot.add_cog(Lock(bot))
    bot.add_cog(Ping(bot))
    bot.add_cog(Report(bot))
    bot.add_cog(Logs(bot))
