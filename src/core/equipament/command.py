import discord

from clientConfig import client
from core.equipament.armor.service import get_armor
from core.equipament.weapon.service import get_weapon
from core.equipament.esoteric.service import get_esoteric, search_esoteric, esotericAutoComplete, embed_esoteric

@client.slash_command(
    name = "gerar_armadura",
    description = "Gera uma armadura com base na 'Tabela 8-4: Equipamento' de Tormenta20",
    guild_ids=[563153398392684554] 
)
async def armor(
    ctx
):
    embed = await get_armor()
    return await ctx.respond(embed = embed)

@client.slash_command(
    name = "gerar_arma",
    description = "Gera uma arma com base na 'Tabela 8-4: Equipamento' de Tormenta20",
    guild_ids=[563153398392684554] 
)
async def weapons(
    ctx
):
    embed = await get_weapon()
    return await ctx.respond(embed = embed)

@client.slash_command(
    name = "gerar_esoterico",
    description = "Gera um item esoterico com base na 'Tabela 8-4: Equipamento' de Tormenta20",
    guild_ids=[563153398392684554] 
)
async def esoteric(
    ctx
):
    embed = await get_esoteric()
    return await ctx.respond(embed = embed)

@client.slash_command(
    name = "busca_esoterico",
    description="Retorna informação do item esoterico escolhido.",
    guild_ids=[563153398392684554] 
)
async def searchEsoteric(
    ctx,
    esoterico: str = discord.Option(
        description="Nome do item.",
        autocomplete=esotericAutoComplete,
    )
):
    id = await search_esoteric(esoterico)
    if(id == None):
        return await ctx.respond("Essa magia não existe")

    embed = await embed_esoteric(id)
    return await ctx.respond(embed = embed)