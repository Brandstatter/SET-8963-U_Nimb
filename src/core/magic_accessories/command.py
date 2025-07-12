import discord

from clientConfig import client
from core.magic_accessories.service import search_acessories, embed_accessory, acessory_autocomplete

@client.slash_command(
    name="busca_acessorio",
    description="Busca um acessorio magico.",
    guilds = [563153398392684554]
) 
async def search_accessory_slash_command(
    ctx,
    acessorio_option: str = discord.Option(
        description="Escolha um acessorio",
        autocomplete=acessory_autocomplete,
    )
):
    id = await search_acessories(acessorio_option)
    if(id == None):
        return await ctx.respond("Esse acessório não existe")

    embed = await embed_accessory(id)
    return await ctx.respond(embed = embed)
    