import discord

from clientConfig import client
from core.chaos_cards.service import draw_cards

@client.slash_command(
    name="baralho_caos",
    description="Saca as cartas do baralho do caos de acordo com quantidade escolhida."
) 
async def chaos_card_slash_command(ctx,
    quantidade_cartas: int = discord.Option(int, choices = [1, 2, 3, 4]                               
    )):
    embed = await draw_cards(quantidade_cartas)
    await ctx.respond(embed = embed)