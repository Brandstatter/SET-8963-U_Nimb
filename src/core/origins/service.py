import os
import json
import discord

from unidecode import unidecode

json_path = os.path.join("json", "origins.json")
ORIGINS_JSON = json.load(open(json_path, encoding='utf-8'))

async def slash_search(chosen_origin):
    for origin in ORIGINS_JSON:
        if (origin['name'] == chosen_origin):
            return origin["id"]

async def embed_origin(id):
    name = str(ORIGINS_JSON[id]['name']).encode('latin-1')

    origin = discord.Embed(
    title = name.decode('latin-1'),
    description = str(ORIGINS_JSON[id]['desc']),
    color = discord.Color.random()
    )

    origin.add_field(name= "Itens", value= str(ORIGINS_JSON[id]['itens']), inline=False)

    origin.add_field(name= "Pericias treinadas", value= str(ORIGINS_JSON[id]['pericias']), inline=False)

    x = 0
    while x < len(ORIGINS_JSON[id]['powerList']):
        origin.add_field(name=str(ORIGINS_JSON[id]['powerList'][x]), value=str(ORIGINS_JSON[id]['powerDesc'][x]), inline=False)
        x = x+1

    return origin

async def origins_autocomplete(ctx: discord.AutocompleteContext):
    query = ctx.value.lower()
    options = [
        origin["name"] for origin in ORIGINS_JSON
        if query in origin["name"].lower()
    ]
    return options[:25]