import discord

class Paginator(discord.ui.View):
    def __init__(self, embeds):
        super().__init__(timeout=180) # Adiciona um tempo limite para a interação
        self.embeds = embeds
        self.page = len(embeds) - 1
        self.update_buttons()

    def update_buttons(self):
        pass

    @discord.ui.button(label="Anterior", style=discord.ButtonStyle.primary, emoji="⬅️")
    async def previous(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.page == 0:
            self.page = len(self.embeds) - 1
        else:
            self.page -= 1
        await interaction.response.edit_message(embed=self.embeds[self.page], view=self)

    @discord.ui.button(label="Próxima", style=discord.ButtonStyle.primary, emoji="➡️")
    async def next(self, button: discord.ui.Button, interaction: discord.Interaction):
        if self.page == len(self.embeds) - 1:
            self.page = 0
        else:
            self.page += 1
        await interaction.response.edit_message(embed=self.embeds[self.page], view=self)

    @discord.ui.button(label="Resultado", style=discord.ButtonStyle.secondary, emoji="📜")
    async def home(self, button: discord.ui.Button, interaction: discord.Interaction):
        self.page = len(self.embeds) - 1
        await interaction.response.edit_message(embed=self.embeds[self.page], view=self)

    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)