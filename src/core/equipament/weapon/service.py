import os
import discord
import json
import random

json_path = os.path.join("json", "equipament/weapon.json")
WEAPON_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "equipament/weapon_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def get_weapon():

    d100 = random.randint(1, 100)

    for item in TABLE_JSON:
        if d100 <= item['cutoffValue']:
            return await embed_weapon(item['rewardId'])
        
async def search_weapon(chosen_weapon: str):
    for weapon in WEAPON_JSON:
        if(weapon["name"] == chosen_weapon):
            return weapon["id"]

async def embed_weapon(id):

    weapon = WEAPON_JSON[id]

    embed = discord.Embed(
        title = f"{weapon['name']}",
        description= f"**{weapon['proficiency']} - {weapon['weaponType']} - {weapon['grip']}**",
        color=discord.Color.random()
    )

    stats = ""

    if weapon.get('damage'):
        stats += (
            f"Dano: {weapon['damage']} | "
            f"Crítico: {weapon['critical']} | "
            f"Tipo de Dano: {weapon['damageType']}\n"
        )

    cost = weapon.get('cost', 'N/A')
    spaces = weapon.get('spaces', 'N/A')
    weapon_range = weapon.get('range')

    if weapon_range:
        stats += f"Valor: {cost} | Alcance: {weapon_range} | Espaço no inventário: {spaces}"
    else:
        stats += f"Valor: {cost} | Espaço no inventário: {spaces}"

    embed.add_field(name= "Características", value= stats, inline= False)
    embed.add_field(name= "Descrição", value= weapon['desc'], inline= False)   

    return embed

async def weaponAutoComplete(ctx: discord.AutocompleteContext):    
    query = ctx.value.lower()
    options = [
        weapon["name"] for weapon in WEAPON_JSON
        if query in weapon["name"].lower()
    ]
    return options[:25]