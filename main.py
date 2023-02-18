import discord
import os
import dotenv

dotenv.load_dotenv()
token = str(os.getenv('TOKEN'))

main_dir = '/root/Development/kamachi/fumiko/'

# init intents
intents = discord.Intents.all()

# init the bot
bot = discord.AutoShardedBot(
    command_prefix=">",
    intent=intents,
    debug_guilds=None
)

cogs_list = []
cogs = os.listdir(f'{main_dir}cogs/')

for f in cogs:
    cog = f.removesuffix('.py')
    cogs_list.append(cog)

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(token)
