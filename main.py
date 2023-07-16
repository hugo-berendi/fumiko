from threading import Thread
import discord
from discord.ext import commands
import os
import dotenv
from web import create_web
from utils.cogs import load_cogs

# set dev dir
os.chdir('/home/kamachi/Development/fumiko')

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


# Threads
web = open('/home/kamachi/Development/fumiko/web/app.py').read()
threads = [Thread(target=bot.run, args=(token,)), Thread(target=exec, args=(web,))]


# main function
def main():
    exec(open('/home/kamachi/Development/fumiko/web/create_web.py').read())
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


# run if __name__ is equal to '__main__'
if __name__ == '__main__':
    main()
