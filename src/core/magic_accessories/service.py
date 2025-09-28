import os
import discord
import json
import random
import math

from discord.ui import View

json_path = os.path.join("json", "magic_accessories.json")
ACESSORIES_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "magic_accessories_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def search_accessories(chosen: str):
    for accessory in ACESSORIES_JSON:
        if(accessory["name"] == chosen):
            return accessory["id"]
    return None

async def embed_accessory(id):

    name = ACESSORIES_JSON[id]["name"]
    description = f'{ACESSORIES_JSON[id]["desc"]} \n\n Valor: {ACESSORIES_JSON[id]["cost"]}'

    embed = discord.Embed(
    title = name,
    description = description,
    color=discord.Color.random())

    return embed

async def accessory_autocomplete(ctx: discord.AutocompleteContext):    
    query = ctx.value.lower()
    options = [
        accessories["name"] for accessories in ACESSORIES_JSON
        if query in accessories["name"].lower()
    ]
    return options[:25]

async def roll_accessory(table):
    d100 = random.randrange(1,101)

    for item in TABLE_JSON[table]['probability']:
            if d100 <= item['cutoffValue']:
                rewardId = item['rewardId']
                break 

    return await embed_accessory(rewardId)