import discord
from discord.ext import commands
import requests

class Destiny(commands.Cog):
    def __init__(self, bot: discord.AutoShardedBot):
        self.bot = bot

    @commands.slash_command(name='destiny', description='This is a destiny test command!')
    async def destiny(self, ctx, id: int):
        #dictionary to hold extra headers
        HEADERS = {"X-API-Key":'cf8afac55d2c42ebbbe8cf83d6fdf367'}

        #make request for Gjallarhorn
        r = requests.get(f"https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/{id}/", headers=HEADERS)
        inventoryItem = r.json()
        await ctx.respond(inventoryItem['Response']['data']['inventoryItem']['itemName'])

def setup(bot):
    bot.add_cog(Destiny(bot))