import discord
import numpy
import random
from discord.ext import commands, tasks


class Tasks(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.status.start()

    @tasks.loop(minutes=2)
    async def status(self):
        stati = [
            discord.Status.idle,
            discord.Status.dnd,
            discord.Status.online
        ]

        members = []
        for guild in self.bot.guilds:
            members.append(guild.member_count)
        
        all_member_count = 0
        for member_count in members:
            all_member_count = all_member_count + member_count

        activities = [
            discord.Game("by Kamachi"),
            discord.Game(f"mit {len(self.bot.guilds)} servern"),
            discord.Game(f"mit {all_member_count} usern")
        ]

        await self.bot.change_presence(status=random.choice(stati),
                                       activity=random.choice(activities))

def setup(bot):
    bot.add_cog(Tasks(bot))
