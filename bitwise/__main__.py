import discord
from discord.ext import commands
from config import config


async def determine_prefix(bot, message):
    prefixes = [f"<@{bot.user.id}>"]
    if (guild := message.guild) and (role := guild.self_role):
        prefixes.append(role.mention)

    return prefixes


class ShardedBot(commands.AutoShardedBot):
    def __init__(self, **kwargs) -> None:
        self.config = kwargs.pop("config", None)
        if not self.config:
            self.config = __import__("config")

        super().__init__(
            **kwargs, command_prefix=determine_prefix, strip_after_prefix=True
        )

        self.add_check(
            commands.bot_has_permissions(
                administrator=True,
            ).predicate
        )

        self.activity = discord.Game("@Bitwise help")

        self.run(kwargs["token"])


if __name__ == "__main__":
    ShardedBot(
        token=config.BOT_TOKEN,
        intents=discord.Intents.all(),
    )
