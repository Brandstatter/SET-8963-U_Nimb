from clientConfig import client
from core.equipament.armor.service import get_armor

@client.slash_command(
    name = "gerar_armadura",
    description = "Gera uma recompensa com base na 'Tabela 8-4: Equipamento' de Tormenta20",
    guild_ids=[563153398392684554] 
)
async def itens(
    ctx
):
    embed = await get_armor()
    return await ctx.respond(embed = embed)