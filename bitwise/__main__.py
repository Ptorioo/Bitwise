import discord
from meta.core import Bitwise
from helper.config import Config


if __name__ == "__main__":
    with Bitwise(
        intents=discord.Intents.all()
    ) as bot:
        bot.run(token=Config.BOT_TOKEN, log_handler=None)
