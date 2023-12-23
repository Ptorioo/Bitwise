import os
import discord
from discord.ext import commands
from discord.message import Message
from .settings import Settings
from helper.logger import logger
import aiohttp

class Bitwise(commands.AutoShardedBot):
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __init__(
        self,
        intents: discord.Intents,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            intents=intents,
            command_prefix=Settings.get_prefix,
            strip_after_prefix=True,
            *args,
            **kwargs,
        )

        self.add_check(
            commands.bot_has_permissions(
                administrator=True,
            ).predicate
        )

        self.activity = discord.Game("@Bitwise help")
        self.session = None

    async def setup_hook(self):
        for root, _, files in os.walk("bitwise/cogs"):
            for file in files:
                if not file.endswith(".py") or file[:-3] == "__init__":
                    continue

                name = file[:-3]
                file_path = os.path.join(root, file)
                directory_name = os.path.basename(os.path.dirname(file_path))

                logger.info(f"cogs.{directory_name}.{name} loaded.")
                await self.load_extension(f"cogs.{directory_name}.{name}")
        
        try:
            synced = await self.tree.sync()
            logger.info(f"Synced {len(synced)} command(s).")
        except Exception as e:
            logger.info(f"Error: {e}")        

        self.session = aiohttp.ClientSession()
        
        await self.load_extension("jishaku")

    async def on_ready(self):
        logger.info(f"{self.user} is running!")

    async def on_message(self, message: Message):
        return await super().on_message(message)
    
    async def close(self):
        await super().close()
        await self.session.close()
