from .directory import Path
from discord.ext.commands import Bot
from discord import Intents
from json import load


with open(Path.ConfigPath(),'r+') as file:
    config = load(file)
    prefix = config['prefix']

bot = Bot(
    command_prefix=prefix,
    help_command=None,
    case_insensitive=True,
    strip_after_prefix = True,
    intents = Intents.all(),
    self_bot=False
)