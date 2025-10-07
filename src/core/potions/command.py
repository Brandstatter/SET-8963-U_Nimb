from clientConfig import client

from core.potions.service import get_potion

@client.slash_command(
    name = "rolar_pocao",
    description = "Gera uma recompensa com base na 'Tabela 8-12: Poções' de Tormenta20"    
)
async def slash_potion(ctx,
    quantidade : int
                       ):
    if quantidade > 10:
        await ctx.respond("Limite de criação de poções execedido. Limite maximo: 10 poções")
    embed = await get_potion(quantidade, False)
    await ctx.respond(embed = embed)