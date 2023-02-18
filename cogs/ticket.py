import discord
from discord.ext import commands

class Ticket(commands.Cog):
    def __init__(self, bot: discord.AutoShardedBot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Ticket(bot))
    
