import os
import discord
import json
import random

json_path = os.path.join("json", "diverse.json")
ITENS_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "diverse_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def get_itens():

    d100 = random.randint(1, 100)

    for item in TABLE_JSON:
        if d100 <= item['cutoffValue']:
            return await embed_item(item['rewardId'])


async def embed_item(id):
    
    embed = discord.Embed(
        title = f"{ITENS_JSON[id]['name']}",
        description= f"**{ITENS_JSON[id]['type']}** \n **Espaço no inventario: **{str(ITENS_JSON[id]['space'])} | **Valor: **{ITENS_JSON[id]['cost']} \n {ITENS_JSON[id]['desc']}",
        color=discord.Color.random()
    )

    return embed