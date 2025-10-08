import os
import discord
import json
import random

json_path = os.path.join("json", "equipament/armor.json")
ARMOR_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "equipament/armor_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def get_armor():
    
    d100 = random.randint(1, 100)

    for item in TABLE_JSON:
        if d100 <= item['cutoffValue']:
            return await embed_armor(item['rewardId'])
        

async def embed_armor(id):

    armor = ARMOR_JSON[id]

    embed = discord.Embed(
        title = f"{armor['name']}",
        description= f"**{armor['type']}**",
        color=discord.Color.random()
    )

    embed.add_field(name="Características", value=f"**Penalidade de Armadura: **{str(armor['penalty'])} | **Bônus na Defesa: **{str(armor['defense'])} \n **Espaço no inventario: **{str(armor['spaces'])} | **Valor: **{armor['cost']}", inline=False)
    embed.add_field(name="Descrição", value= armor['desc'], inline=False)

    return embed