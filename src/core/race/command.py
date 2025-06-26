import discord

from clientConfig import client
from core.race.service import embed_race

@client.slash_command(
    name = "races",
    description = "Retorna atributos e habilidades da raça selecionada.",
    guild_ids = guilds_list
)
async def slash_race(ctx,
    race_option : str = discord.Option(str, choices = ['Humano', 'Anão', 'Dahllan', 'Elfo', 'Goblin', 'Lefou', 'Minotauro', 'Qareen', 'Golem', 'Hynne', 'Kliren', 'Medusa', 'Osteon', 'Sereia/Tritão', 'Sílfide', 'Suraggel', 'Trog', 'Eiradaan', 'Galokk', 'Meio-Elfo', 'Sátiro'])
):
    options = ['Humano', 'Anão', 'Dahllan', 'Elfo', 'Goblin', 'Lefou', 'Minotauro', 'Qareen', 'Golem', 'Hynne', 'Kliren', 'Medusa', 'Osteon', 'Sereia/Tritão', 'Sílfide', 'Suraggel', 'Trog', 'Eiradaan', 'Galokk', 'Meio-Elfo', 'Sátiro']
    embed = await embed_race(ctx, options.index(race_option))
    await ctx.respond(embed = embed)