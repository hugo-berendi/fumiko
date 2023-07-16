import discord
from enum import Enum


class EmbType(Enum):
    ERROR = discord.Colour.brand_red()
    SUCCESS = discord.Colour.green()
    NSFW = discord.Colour.nitro_pink()
    GENERAL = discord.Colour.blue()


def build_embed(emb_type: str, title: str, content: str = ''):
    emb = discord.Embed(
        colour=EmbType[emb_type].value,
        title=title,
        description=content
    )

    emb.timestamp = discord.utils.utcnow()

    return emb
