import uvloop
import logging
import asyncio
import time
from discord.ext import commands

uvloop.install()


class Music(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot


async def setup(bot):
    await bot.add_cog(Music(bot))
