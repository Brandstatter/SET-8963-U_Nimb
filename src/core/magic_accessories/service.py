import os
import discord
import json
import random
import math

from discord.ui import View

json_path = os.path.join("json", "magic_accessories.json")
ACESSORIES_JSON = json.load(open(json_path, encoding='utf-8'))


async def search_accessories(chosen_magic: str):
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

async def accessory_autocomplete(ctx: discord.AutocompleteContext):    
    query = ctx.value.lower()
    options = [
        accessories["name"] for accessories in ACESSORIES_JSON["accessories"]
        if query in accessories["name"].lower()
    ]
    return options[:25]

async def roll_accessory(table):
    d100 = random.randrange(1,100)
    percentages = ACESSORIES_JSON['tables'][table]['percentages']
    print(percentages)
    print(ACESSORIES_JSON['tables'][table]['prizes'])
    index = 0
    # Check if dice roll is higher than each number on percentages.
    while d100 > percentages[index]:
        index += 1
    # Halfes index and round to the lowest number to get index of the reward.
    index = int(math.floor(index/2))

    return await embed_accessory(ACESSORIES_JSON['tables'][table]['prizes'][index])