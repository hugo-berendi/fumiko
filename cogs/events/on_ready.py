import discord
from discord.ext import commands


class Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} is ready with a latency of {self.bot.latency}')


def setup(bot):
    bot.add_cog(Ready(bot))
