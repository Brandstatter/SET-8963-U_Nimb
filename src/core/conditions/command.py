import discord

from clientConfig import client
from core.conditions.service import slash_search, embed_condition, condition_autocomplete

@client.slash_command(
    name = "conditions",
    description = "Envia embed com informações sobre a condição selecionada."
)
async def slash_conditions(
    ctx, 
    condition_option: str = discord.Option(
        description="Condições",
        autocomplete=condition_autocomplete
    )
):
    embed = await execute(ctx, condition_option)
    await ctx.respond(embed = embed)

# @client.command(
#     name="conditions"
# )
# async def conditions_command(ctx, *, arg):
#     embed = await execute(ctx, arg)
#     await ctx.send(embed = embed)

async def execute(ctx, args):
    id = await slash_search(ctx, args)
    embed = await embed_condition(ctx, id)
    return embed