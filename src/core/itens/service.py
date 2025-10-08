import os
import discord
import json
import random

json_path = os.path.join("json", "itens/diverse.json")
ITENS_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "itens/diverse_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def get_itens():

    d100 = random.randint(1, 100)

    for item in TABLE_JSON:
        if d100 <= item['cutoffValue']:
            return await embed_item(item['rewardId'])


async def embed_item(id):

    item = ITENS_JSON[id]
    
    embed = discord.Embed(
        title = f"{item['name']}",
        description= f"**{item['type']}**",
        color=discord.Color.random()
    )

    embed.add_field(name="Características", value= f"**Espaço no inventario: **{str(item['space'])} | **Valor: **{item['cost']}", inline=False)
    embed.add_field(name="Descrição", value= item['desc'], inline=False)

    return embed