import discord
import random

from clientConfig import client
from core.magic.service import embed_magic, search_magic, magicAutoComplete

# Random Magic
@client.command(aliases = ['l', 'random']) 
async def randomMagic(ctx):
    embed = await embed_magic(random.randrange(0, 219))
    await ctx.send(embed = embed)

@client.slash_command(
    name="random_magic",
    description="Busca uma magia aleatoriamente",
) 
async def random_magic_slash_command(ctx):
    embed = await embed_magic(random.randrange(0, 219))
    return await ctx.respond(embed = embed)
    

@client.slash_command(
    name = "searchmagic",
    description="Procura uma magia",    
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
        return await ctx.respond("Magia não existe")

    embed = await embed_magic(id)
    return await ctx.respond(embed = embed)
