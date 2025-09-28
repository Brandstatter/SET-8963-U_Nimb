import os
import discord
import json
import random
import asyncio

json_path = os.path.join("json", "potions.json")
POTION_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "potions_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def get_potion(qtd):

    potion_ids = []
    x = 0

    while x < qtd:
        d100 = random.randrange(1, 100)
        for item in TABLE_JSON:
            if d100 <= item['cutoffValue']:
                potion_ids.append(item['rewardId'])
                break 
        x = x + 1    
    embed = await embed_potion(potion_ids)
    return embed

async def embed_potion(ids):
    ids = [4, 4, 4, 4]
    name = "Poções encontradas"

    embed = discord.Embed(
        title = name,
        description="",
        color=discord.Color.random()
    )

    for id in ids:
        print(id)
        embed.add_field(name=f"{POTION_JSON[id]['name']}", value=f"{POTION_JSON[id]['desc']}\n **Valor**: {POTION_JSON[id]['cost']}", inline=False)

    return embed
