from clientConfig import client
from core.conditions.service import slash_search, embed_condition

@client.slash_command(
    name = "conditions",
    description = "Envia embed com informações sobre a condição selecionada."
)
async def slash_conditions(ctx, 
    condition_option
                           ):
    id = await slash_search(ctx, condition_option)
    embed = await embed_condition(ctx, id)
    await ctx.respond(embed = embed)