import discord

from clientConfig import client
from core.origins.service import slash_search, embed_origin, origins_autocomplete

@client.slash_command(
    name = "origens",
    description = "Informa beneficios e itens da origem selecionada."
)
async def slash_origins(ctx,
    origem: str = discord.Option(str, "Escolha uma origem.", autocomplete=origins_autocomplete)                 
):
    id = await slash_search(origem)
    if(id == None):
        return await ctx.respond("Essa origem não existe")
    embed = await embed_origin(id)
    await ctx.respond(embed = embed)