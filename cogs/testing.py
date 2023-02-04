import discord
from discord.ext import commands

class Testing(commands.Cog):
    def __init__(self, bot: discord.AutoShardedBot):
        self.bot = bot

    @commands.slash_command(name='test', description='This is a test command!')
    async def test(self, ctx):
        await ctx.respond(f'Pong! Latency is {self.bot.latency}')

def setup(bot):
    bot.add_cog(Testing(bot))