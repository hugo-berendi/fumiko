import discord
from discord import ApplicationContext
from discord.ext import commands
from discord.commands import slash_command
from utils.embeds import build_embed


class Help(commands.Cog):
    def __init__(self, bot: discord.Bot):
        self.bot = bot

    @slash_command(description="Send help for commands", name="help")
    async def report(
            self,
            ctx: ApplicationContext,
            args: discord.Option(discord.SlashCommandOptionType.string, "args", required=False, default=None)
    ):
        emb = build_embed('GENERAL', 'Command Help')

        command_names_list = [x.name for x in self.bot.commands]

        if not args:
            emb.add_field(
                name="List of supported commands:",
                value="\n".join([str(i + 1) + ". " + x.name for i, x in enumerate(self.bot.commands)]),
                inline=False
            )
            emb.add_field(
                name="Details",
                value="Type `/help <command name>` for more details about each command.",
                inline=False
            )

        elif args in command_names_list:
            emb.add_field(
                name=args,
                value=self.bot.get_command(args).description
            )
        else:
            emb.add_field(
                name="Oh, no!",
                value="I didn't find command :("
            )

        await ctx.respond(embeds=[emb])


def setup(bot):
    bot.add_cog(Help(bot))
