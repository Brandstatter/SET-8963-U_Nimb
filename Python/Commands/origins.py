import os
import json
import discord

from unidecode import unidecode

json_path = os.path.join("json", "origins.json")
ORIGINS_JSON = json.load(open(json_path, encoding='utf-8'))

async def search_origin(ctx):
    message = unidecode(ctx.message.content)
    message = message[3:]
    print(message)
    list_ids = []
    for origin in ORIGINS_JSON:
        if unidecode(origin['name']).lower().find(message.lower()) == 0:
            list_ids.append(origin['id'])
    if len(list_ids) == 1:
        return list_ids[0]
    else:
        await ctx.send("Encontramos " + str(len(list_ids)) + " origens, por favor seja mais específico.")


async def embed_origin(ctx, id):
    name = str(ORIGINS_JSON[id]['name']).encode('latin-1')

    origin = discord.Embed(
    title = name.decode('latin-1'),
    description = str(ORIGINS_JSON[id]['desc']),
    color = discord.Color.random()
    )

    origin.add_field(name= "Itens", value= str(ORIGINS_JSON[id]['itens']), inline=False)

    origin.add_field(name= "Pericias", value= str(ORIGINS_JSON[id]['pericias']), inline=False)

    x = 0
    while x < len(ORIGINS_JSON[id]['powerList']):
        origin.add_field(name=str(ORIGINS_JSON[id]['powerList'][x]), value=str(ORIGINS_JSON[id]['powerDesc'][x]), inline=False)
        x = x+1

    return origin