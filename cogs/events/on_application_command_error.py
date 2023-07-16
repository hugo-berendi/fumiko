import discord
from discord.ext import commands
from discord.ext.commands import CommandError, NSFWChannelRequired, CommandOnCooldown
from utils.embeds import build_embed


class AppCmdError(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx: discord.ApplicationContext, error: discord.DiscordException):
        if isinstance(error, CommandOnCooldown):
            emb = build_embed('ERROR', 'Command Error', 'This command is currently on cooldown!')
            await ctx.respond(embed=emb, ephemeral=True)
            return
        elif isinstance(error, NSFWChannelRequired):
            emb = build_embed(
                'ERROR',
                'Command Error',
                f'Channel "{error.channel.name}" needs to be NSFW for this command to work.'
            )
            await ctx.respond(embed=emb, ephemeral=True)
            return
        elif isinstance(error, CommandError):
            emb = build_embed('ERROR', 'Command Error', 'An error occurred while processing the command.')
            await ctx.respond(embed=emb, ephemeral=True)
            return
        else:
            raise error


def setup(bot):
    bot.add_cog(AppCmdError(bot))
