import discord

from clientConfig import client
from core.race.service import embed_race

options = ['Humano', 'Anão', 'Dahllan', 'Elfo', 'Goblin', 'Lefou', 'Minotauro', 'Qareen', 'Golem', 'Hynne', 'Kliren', 'Medusa', 'Osteon', 'Sereia/Tritão', 'Sílfide', 'Suraggel', 'Trog', 'Eiradaan', 'Galokk', 'Meio-Elfo', 'Sátiro']
@client.slash_command(
    name = "races",
    description = "Retorna informações sobre a raça escolhida.",
)
async def slash_race(ctx,
    race_option : str = discord.Option(str, choices = options)
):
    embed = await embed_race(ctx, options.index(race_option))
    await ctx.respond(embed = embed)