import discord
import uvloop
import asyncio
from core.bitwise import Bitwise
from helper.config import Config


async def main():
    with Bitwise(intents=discord.Intents.all()) as bot:
        await bot.start(token=Config.BOT_TOKEN)


if __name__ == "__main__":
    try:
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
