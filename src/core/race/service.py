import os

import discord
import json

json_path = os.path.join("json", "races/races.json")
RACES_JSON = json.load(open(json_path, encoding='utf-8'))

async def embed_race(ctx, id):
    name = str(RACES_JSON[id]['name']).encode('latin-1')
    atribute = str(RACES_JSON[id]['atributes']).encode('latin-1')

    race = discord.Embed(
    title = name.decode('latin-1'),
    description = "**Atributos** \n" + atribute.decode('latin-1'),
    color = discord.Color.random()
    )

    x = 0
    while x < len(RACES_JSON[id]['skills']['titles']):
        race.add_field(name=str(RACES_JSON[id]['skills']['titles'][x]), value=str(RACES_JSON[id]['skills']['description'][x]), inline=False)
        x = x+1

    return race
    