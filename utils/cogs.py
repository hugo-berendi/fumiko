import os
import discord


def load_cogs(bot: discord.Bot, cog_dir: str):
    dirs = os.listdir(cog_dir)

    for dir in dirs:
        cogs = os.listdir(f'{cog_dir}{dir}/')
        for f in cogs:
            cog = f.removesuffix('.py')
            if cog == '__pycache__':
                continue
            bot.load_extension(f'cogs.{dir}.{cog}')
            print(f'% Loaded "{cog}"')