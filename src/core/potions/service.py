import os
import discord
import json
import random

json_path = os.path.join("json", "potions.json")
POTION_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "potions_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def get_potion():

    d100 = random.randrange(1, 100)

    for item in TABLE_JSON:
            if d100 <= item['cutoffValue']:
                embed = await embed_potion(item['rewardId'])
                break 

    return embed

async def embed_potion(id):

    name = POTION_JSON[id]["name"]
    description = f'{POTION_JSON[id]["desc"]} \n\n Valor: {POTION_JSON[id]["cost"]}'

    embed = discord.Embed(
    title = name,
    description = description,
    color=discord.Color.random())

    return embed