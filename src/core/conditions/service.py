import os

import discord
import json

from unidecode import unidecode

json_path = os.path.join("json", "conditions/conditions.json")
COND_JSON = json.load(open(json_path, encoding='utf-8'))

async def slash_search(ctx, choice):
    for condition in COND_JSON:
        if condition["name"].lower() == choice.lower():
            return condition["id"]
        
    return None

# Function that creates the embed of the condition based on id.
async def embed_condition(ctx, id):
    # Block of code that pulls specifics data for the embed. (Enconding in latin necessary to accents.)
    name = str(COND_JSON[id]['name'])
    type_cond = str(COND_JSON[id]['typeC'])
    text = str(COND_JSON[id]['text'])
    subtext = str(COND_JSON[id]['subtext'])

    # Conditions embed body
    conditions = discord.Embed(
    title = name,
    description = type_cond,
    color = discord.Color.random())
    
    # Work around subtext existence or not
    if subtext == None:
        conditions.add_field(name="Efeitos", value= text, inline=False)
    else:
        conditions.add_field(name="Efeitos", value= text + '\n' + str(subtext), inline=False)
    
    return conditions

async def condition_autocomplete(ctx: discord.AutocompleteContext):
    query = ctx.value.lower()
    options = [
        condition["name"] for condition in COND_JSON
        if query in condition["name"].lower()
    ]
    return options[:25]
