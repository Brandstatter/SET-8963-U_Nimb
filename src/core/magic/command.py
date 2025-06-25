import random

from clientConfig import client
from core.magic.service import embed_magic, search_magic

# Random Magic
@client.command(aliases = ['l', 'random']) 
async def randomMagic(ctx):
    embed = await embed_magic(random.randrange(0, 197))
    await ctx.send(embed = embed)
 
# Search Magic
@client.command(aliases = ['e', 'magia']) 
async def searchMagic(ctx, name:str):
    id = await search_magic(ctx)
    for magic in id:
        embed = await embed_magic(magic)
        await ctx.send(embed = embed)