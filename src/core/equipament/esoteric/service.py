import os
import discord
import json
import random

json_path = os.path.join("json", "equipament/esoteric.json")
ESOTERIC_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "equipament/esoteric_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def get_esoteric():

    d100 = random.randint(1, 100)

    for item in TABLE_JSON:
        if d100 <= item['cutoffValue']:
            return await embed_esoteric(item['rewardId'])
        
async def search_esoteric(chosen_esoteric: str):
    for esoteric in ESOTERIC_JSON:
        if(esoteric["name"] == chosen_esoteric):
            return esoteric["id"]
        
async def embed_esoteric(id):

    esoteric = ESOTERIC_JSON[id]

    embed = discord.Embed(
        title = f"{esoteric['name']}",
        description= f"{esoteric['desc']} \n **Valor:** {esoteric['cost']}",
        color=discord.Color.random()
    )

    return embed

async def esotericAutoComplete(ctx: discord.AutocompleteContext):    
    query = ctx.value.lower()
    options = [
        esoteric["name"] for esoteric in ESOTERIC_JSON
        if query in esoteric["name"].lower()
    ]
    return options[:25]