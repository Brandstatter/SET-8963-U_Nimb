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

    embed = discord.Embed(
        title = f"{ARMOR_JSON[id]['name']}",
        description= f"**{ARMOR_JSON[id]['type']}** \n **Penalidade de Armadura: **{str(ARMOR_JSON[id]['penalty'])} | **Bônus na Defesa: **{str(ARMOR_JSON[id]['defense'])} \n **Espaço no inventario: **{str(ARMOR_JSON[id]['spaces'])} | **Valor: **{ARMOR_JSON[id]['cost']} \n {ARMOR_JSON[id]['desc']}",
        color=discord.Color.random()
    )

    return embed