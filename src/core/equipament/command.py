from clientConfig import client
from core.equipament.armor.service import get_armor
from core.equipament.weapon.service import get_weapon

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