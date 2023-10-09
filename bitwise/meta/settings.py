class Settings:
    def __init__(self) -> None:
        pass

    async def get_prefix(bot, ctx):
        prefixes = [f"<@{bot.user.id}>"]
        if (guild := ctx.guild) and (role := guild.self_role):
            prefixes.append(role.mention)

        return prefixes
