import discord

from clientConfig import client
from core.reward.service import get_percent
from core.reward.new_service import get_treasure, embed_fail

options = ['1/4', '1/2', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

@client.slash_command(
    name = "recompensa_dinheiro",
    description = "Retorna recompensa de dinheiro de acordo com o ND."
)
async def slash_money(ctx: discord.ApplicationContext,
    nd : str = discord.Option(str, choices = options)
):
    
    reward = await get_treasure(nd)
    return await ctx.respond(embed = reward)

    # embed = await get_percent(options.index(nd))
    # await ctx.respond(embed = embed)