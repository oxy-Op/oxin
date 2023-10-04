from json import load
from os import getcwd

class Path:
    """A class that used to define config files path"""

    def ConfigPath(path='/config/config.json'):
        """Path to config.json Parameters : \n path: `fp` - file path for config"""
        return "".join(getcwd() + path)

    def SettingsPath(path="/settings/botsettings.json"):
        """Path to settings.json Parameters : \n path : `fp` """
        return "".join(getcwd() + path)

    def DataBasePath(path='/database/discordlogs.db'):
        """Path to database : parameters : \n path : `fp` """
        return "".join(getcwd() + path)

