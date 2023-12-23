import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot
    
    @commands.hybrid_command(
            name='test',
            description='test',
    )
    async def test(self, ctx):
        await ctx.send("lol")

async def setup(bot):
    await bot.add_cog(Help(bot))