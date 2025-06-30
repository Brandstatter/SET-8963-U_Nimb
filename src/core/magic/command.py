import discord
import random

from clientConfig import client
from core.magic.service import embed_magic, search_magic, magicAutoComplete

# Random Magic
@client.slash_command(
    name="random_magic",
    description="Busca uma magia aleatoriamente.",
) 
async def random_magic_slash_command(ctx):
    embed = await embed_magic(random.randrange(0, 219))
    return await ctx.respond(embed = embed)
    
# Search magic
@client.slash_command(
    name = "busca_magia",
    description="Retorna informação da Magia escolhida.",    
)
async def searchMagicSlashCommand(
    ctx,
    magic_option: str = discord.Option(
        description="Escolha a magia",
        autocomplete=magicAutoComplete,
    )
):
    id = await search_magic(magic_option)
    if(id == None):
        return await ctx.respond("Essa magia não existe")

    embed = await embed_magic(id)
    return await ctx.respond(embed = embed)
