import discord
from discord import ApplicationContext
from discord.ext import commands
from utils.modals import ReportModal


class Report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    report_commands = discord.SlashCommandGroup('report', 'Report something')

    @report_commands.command(description="Report an user", name="user")
    async def report(
            self,
            ctx: ApplicationContext,
            reason: discord.Option(str, choices=['Spam', 'Voice Changer', 'Phishing', 'Racist Statement']),
            user: discord.Option(discord.SlashCommandOptionType.user)
    ):
        modal = ReportModal(title="User Report Form", reason=reason, user=user)
        await ctx.send_modal(modal)


def setup(bot):
    bot.add_cog(Report(bot))
