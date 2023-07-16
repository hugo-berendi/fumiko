import discord


class ReportModal(discord.ui.Modal):
    def __init__(self, reason: str, user: discord.User, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.reason = reason
        self.user = user
        self.add_item(discord.ui.InputText(label="Description", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=f'Report by {interaction.user.name}#{interaction.user.discriminator}',
            color=discord.Colour.dark_gold()
        )
        embed.add_field(name="Reported User", value=f'{self.user.mention}', inline=False)
        embed.add_field(name="Report Reason", value=self.reason, inline=False)
        embed.add_field(name="Report Description", value=self.children[0].value, inline=False)
        await interaction.guild.get_channel(1103723173846995054).send(embeds=[embed])
        await interaction.respond('Thank you for your report! :)', ephemeral=True)
