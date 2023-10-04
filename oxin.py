from extras.credentials import Credentials
from extras.bot import bot
import asyncio

bot = bot


async def Init():
    async with bot:
        await bot.load_extension("commands.__init__")
        await bot.load_extension("events.__init__")
        await bot.start(Credentials._token(), reconnect=True)


if __name__ == "__main__":
    asyncio.run(Init())
