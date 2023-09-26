from threading import Thread
import discord
from discord.ext import commands
import os
import dotenv
from web import create_web
from utils.cogs import load_cogs

# set dev dir
os.chdir('/root/dev/fumiko')

# env vars
env = dotenv.dotenv_values(f'{os.getcwd()}/.env')
token = str(env['TOKEN'])

# set intents
intents = discord.Intents.all()

# init the bot
bot = discord.Bot(
    intent=intents,
    debug_guilds=None,
    help_command=commands.DefaultHelpCommand()
)

cog_dir = f'{os.getcwd()}/cogs/'
load_cogs(bot, cog_dir)

# run if __name__ is equal to '__main__'
if __name__ == '__main__':
    bot.run(token)
