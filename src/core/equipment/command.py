import discord

from clientConfig import client
from core.equipment.armor.service import generate_armor, search_armor, armorAutoComplete, embed_armor
from core.equipment.weapon.service import generate_weapon, search_weapon, weaponAutoComplete, embed_weapon
from core.equipment.esoteric.service import generate_esoteric, search_esoteric, esotericAutoComplete, embed_esoteric
from core.equipment.service import get_type

@client.slash_command(
    name = "gerar_armadura",
    description = "Gera uma armadura com base na 'Tabela 8-4: Equipamento' de Tormenta20",
    guild_ids=[563153398392684554] 
)
async def generate_armor(
    ctx
):
    embed = await generate_armor()
    return await ctx.respond(embed = embed)

@client.slash_command(
    name = "busca_armadura",
    description="Retorna informação do item armadura escolhido.",
    guild_ids=[563153398392684554] 
)
async def search_armor(
    ctx,
    armadura: str = discord.Option(
        description="Nome do item.",
        autocomplete=armorAutoComplete,
    )
):
    id = await search_armor(armadura)
    if(id == None):
        return await ctx.respond("Essa armadura não existe")

    embed = await embed_armor(id)
    return await ctx.respond(embed = embed)

@client.slash_command(
    name = "gerar_arma",
    description = "Gera uma arma com base na 'Tabela 8-4: Equipamento' de Tormenta20",
    guild_ids=[563153398392684554] 
)
async def generate_weapon(
    ctx
):
    embed = await generate_weapon()
    return await ctx.respond(embed = embed)

@client.slash_command(
    name = "busca_arma",
    description="Retorna informação do item arma escolhido.",
    guild_ids=[563153398392684554] 
)
async def search_weapon(
    ctx,
    arma: str = discord.Option(
        description="Nome do item.",
        autocomplete=weaponAutoComplete,
    )
):
    id = await search_weapon(arma)
    if(id == None):
        return await ctx.respond("Essa arma não existe")

    embed = await embed_weapon(id)
    return await ctx.respond(embed = embed)

@client.slash_command(
    name = "gerar_esoterico",
    description = "Gera um item esoterico com base na 'Tabela 8-4: Equipamento' de Tormenta20",
    guild_ids=[563153398392684554] 
)
async def generate_esoteric(
    ctx
):
    embed = await generate_esoteric()
    return await ctx.respond(embed = embed)

@client.slash_command(
    name = "busca_esoterico",
    description="Retorna informação do item esoterico escolhido.",
    guild_ids=[563153398392684554] 
)
async def search_esoteric(
    ctx,
    esoterico: str = discord.Option(
        description="Nome do item.",
        autocomplete=esotericAutoComplete,
    )
):
    id = await search_esoteric(esoterico)
    if(id == None):
        return await ctx.respond("Esse item não existe")

    embed = await embed_esoteric(id)
    return await ctx.respond(embed = embed)

@client.slash_command(
    name = "gera_equipamento",
    description="Gera uma recompensa de equipamento com base na descrição da pagina 330 de Tormenta20.",
    guild_ids=[563153398392684554] 
)
async def generate_equipment(
    ctx
    ):
    embed = await get_type()
    return await ctx.respond(embed = embed)