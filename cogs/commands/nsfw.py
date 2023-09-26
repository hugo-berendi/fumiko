import discord
from discord import ApplicationContext, SlashCommandGroup
from discord.ext import commands
import asyncpraw
import os
import dotenv
import random
from utils.embeds import *
import requests
from main import env


class NSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    nsfw_commands: SlashCommandGroup = discord.SlashCommandGroup('nsfw', 'All NSFW commands')

    @nsfw_commands.command(description="Random hentai image via reddit", name="reddit_hentai")
    @commands.is_nsfw()
    async def report(
            self,
            ctx: ApplicationContext,
    ):
        await ctx.defer()
        emb = build_embed('ERROR', 'Reddit API Costs')
        emb.description = 'Due to changes in Reddit Agbs the Api for this command costs to much for us and have to disable this command. :('
        await ctx.respond(embeds=[emb])
        /*
        async with asyncpraw.Reddit(
                client_id='Zs_FRxeC1Synq6a_XElsNQ',
                client_secret=env['REDDIT_SECRET'],
                username='kamachi_der_magier',
                password='Gj?f-B}Q]iV8)LN',
                user_agent=''
        ) as reddit:
            subreddits = [
                {
                    'name': 'hentai',
                    'priority': 0.3
                },
                {
                    'name': 'doujinshi',
                    'priority': 0.15
                },
                {
                    'name': 'HENTAI_GIF',
                    'priority': 0.05
                },
                {
                    'name': 'WesternHentai',
                    'priority': 0.1
                },
                {
                    'name': 'thick_hentai',
                    'priority': 0.1
                },
                {
                    'name': 'wholesomehentai',
                    'priority': 0.2
                },
                {
                    'name': 'Tentai',
                    'priority': 0.1
                },
            ]

            posts = []
            for subreddit in subreddits:
                loaded_subreddit = await reddit.subreddit(subreddit['name'])
                hot = loaded_subreddit.hot(limit=100*subreddit['priority'])

                async for post in hot:
                    if not post.is_video:
                        posts.append({
                            'post': post,
                            'subreddit': subreddit['name']
                        })

            random_post = random.choice(posts)

            emb = build_embed('NSFW', f'{random_post["post"].title}')
            emb.set_image(url=random_post['post'].url)
            emb.set_footer(text=f'from r/{random_post["subreddit"]}', icon_url='')

            await ctx.respond(embeds=[emb])
        */

    @nsfw_commands.command(description="Hentai image with custom type", name="hentai")
    @commands.is_nsfw()
    async def report(
            self,
            ctx: ApplicationContext,
            tag: discord.Option(
                str, choices=[
                    'blowjob',
                    'cum',
                    'feet',
                    'hentai',
                    'wallpapers',
                    'spank',
                    'gasm',
                    'lesbian',
                    'lewd',
                    'pussy'
                ]
            ),
    ):
        req = requests.get(f'http://api.nekos.fun:8080/api/{tag}').json()
        url: str = req['image']

        emb = build_embed('NSFW', f'Hentai Tag: {tag}')
        emb.set_image(url=url)

        await ctx.respond(embeds=[emb])


def setup(bot):
    bot.add_cog(NSFW(bot))
