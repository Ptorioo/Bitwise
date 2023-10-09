import os
from logger import Logger
import discord
from discord.ext import commands
from config import Config

log = Logger()

async def determine_prefix(bot, message):
    prefixes = [f"<@{bot.user.id}>"]
    if (guild := message.guild) and (role := guild.self_role):
        prefixes.append(role.mention)

    return prefixes


class ShardedBot(commands.AutoShardedBot):
    def __init__(self, **kwargs) -> None:
        super().__init__(
            command_prefix=determine_prefix, strip_after_prefix=True, **kwargs
        )

        self.add_check(
            commands.bot_has_permissions(
                administrator=True,
            ).predicate
        )

        self.activity = discord.Game("@Bitwise help")

        self.run(kwargs["token"], log_handler=None)
    
    async def setup_hook(self):
        for root, _, files in os.walk("bitwise/cogs"):
            for file in files:
                if not file.endswith(".py") or file[:-3] == "__init__":
                    continue

                name = file[:-3]
                file_path = os.path.join(root, file)
                directory_name = os.path.basename(os.path.dirname(file_path))

                log.logger.info(f"cogs.{directory_name}.{name} loaded.")
                await self.load_extension(f"cogs.{directory_name}.{name}")

    async def on_ready(self):
        log.logger.info(f"{self.user} is running!")


if __name__ == "__main__":
    ShardedBot(token=Config.BOT_TOKEN, intents=discord.Intents.all())
