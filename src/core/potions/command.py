from clientConfig import client

from core.potions.service import get_potion

@client.slash_command(
    name = "rolar_pocao",
    description = "Retorna recompensa de dinheiro de acordo com o ND."    
)
async def slash_potion(ctx,
    quantidade : int
                       ):
    if quantidade > 10:
        await ctx.respond("Limite de criação de poções execedido. Limite maximo: 10 poções")
    embed = await get_potion(quantidade)
    await ctx.respond(embed = embed)