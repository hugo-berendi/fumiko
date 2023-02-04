import discord
from discord.ext import commands
import pycord.wavelink as wavelink

async def connect_nodes(bot: discord.Bot):
    await bot.wait_until_ready()

    await wavelink.NodePool.create_node(
        bot=bot,
        host='my.tofumc.pro',
        port=25570,
        password='sussy'
    )

class Events(commands.Cog):
    def __init__(self, bot: discord.AutoShardedBot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} is ready with a latency of {self.bot.latency}')
        await connect_nodes(self.bot)

    @commands.Cog.listener()
    async def on_wavelink_node_ready(self, node: wavelink.Node):
        print(f'{node.identifier} is ready!')
    
    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.DiscordException):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.respond('This command is currently on cooldown!')
        else:
            await ctx.respond(f'```\n{error}\n```')

def setup(bot):
    bot.add_cog(Events(bot))
