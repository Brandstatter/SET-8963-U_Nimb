import discord

from clientConfig import client
from core.magic_accessories.service import search_accessories, embed_accessory, accessory_autocomplete, roll_accessory

@client.slash_command(
    name="busca_acessorio",
    description="Retorna informações sobre o acessorio magico escolhido."
) 
async def search_accessory_slash_command(
    ctx,
    acessorio_option: str = discord.Option(
        description="Escolha um acessorio",
        autocomplete=accessory_autocomplete,
    )
):
    id = await search_accessories(acessorio_option)
    if(id == None):
        return await ctx.respond("Esse acessório não existe")

    embed = await embed_accessory(id)
    return await ctx.respond(embed = embed)

@client.slash_command(
    name="rolar_acessorio",
    description="Gera uma recompensa com base nas tabelas 8-13, 8-14 e 8-15 de Acessórios de Tormenta20"
) 
async def search_accessory_slash_command(
    ctx,
    categoria: str = discord.Option(str, choices = ["Acessórios Menores", "Acessórios Médios", "Acessórios Maiores"],
        description="Escolha categoria de acessórios que deseja."
    )
):
    if categoria == "Acessórios Menores":
        embed = await roll_accessory(0)
        await ctx.respond(embed = embed)
    elif categoria == "Acessórios Médios":
        embed = await roll_accessory(1)
        await ctx.respond(embed = embed)
    else:
        embed = await roll_accessory(2)
        await ctx.respond(embed = embed)