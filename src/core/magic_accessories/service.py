import os
import discord
import json
from discord.ui import View

json_path = os.path.join("json", "magic_accessories.json")
ACESSORIES_JSON = json.load(open(json_path, encoding='utf-8'))


async def search_acessories(chosen_magic: str):
    for accessory in ACESSORIES_JSON["accessories"]:
        if(accessory["name"] == chosen_magic):
            return accessory["id"]
    return None

async def embed_accessory(id):

    name = ACESSORIES_JSON["accessories"][id]["name"]
    description = f'{ACESSORIES_JSON["accessories"][id]["desc"]} \n\n Valor: {ACESSORIES_JSON["accessories"][id]["cost"]}'

    embed = discord.Embed(
    title = name,
    description = description,
    color=discord.Color.random())

    return embed

async def acessory_autocomplete(ctx: discord.AutocompleteContext):    
    query = ctx.value.lower()
    options = [
        accessories["name"] for accessories in ACESSORIES_JSON["accessories"]
        if query in accessories["name"].lower()
    ]
    return options[:25]

