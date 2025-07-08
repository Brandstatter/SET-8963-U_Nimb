import discord

from clientConfig import client
from core.conditions.service import slash_search, embed_condition, condition_autocomplete

@client.slash_command(
    name = "condições",
    description = "Envia embed com informações sobre a condição selecionada."
)
async def slash_conditions(
    ctx, 
    condition_option: str = discord.Option(
        description="Condições",
        autocomplete=condition_autocomplete
    )
):
    id = await slash_search(ctx, condition_option)
    if(id == None):
        return await ctx.respond("Condição não encontrada!")
    embed = await embed_condition(ctx, id)
    return await ctx.respond(embed = embed)
  