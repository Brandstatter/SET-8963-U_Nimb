from clientConfig import client
from core.itens.service import get_itens

@client.slash_command(
    name = "itens_diversos",
    description = "Gera uma recompensa com base na 'Tabela 8-3: Itens Diversos' de Tormenta20",
    guild_ids=[563153398392684554] 
)
async def itens(
    ctx
):
    embed = await get_itens()
    return await ctx.respond(embed = embed)