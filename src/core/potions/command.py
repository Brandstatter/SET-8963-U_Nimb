import discord

from clientConfig import client
from core.potions.service import get_potion

@client.slash_command(
    name = "rolar_poção",
    description = "Retorna recompensa de dinheiro de acordo com o ND.",
    
)
async def slash_potion(ctx):
    embed = await get_potion()
    await ctx.respond(embed = embed)