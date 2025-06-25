""" Functions related with spells part of the Magic Madness bot.

Both functions that create the embeded view of a spell based on the id and the de function to search magic are on this module.
"""
import os
import discord
import json
from unidecode import unidecode
from discord.ui import View

json_path = os.path.join("json", "magics.json")
MAG_JSON = json.load(open(json_path, encoding='utf-8'))


# Search a spell by id or name
async def search_magic(ctx):
    #TODO If list of magics is too big, create dropdown menu to choose spell.
    message = unidecode(ctx.message.content)
    message = message[3:]
    spell_ids = []
    # Added a step to verify if spells found exceeds 3, if exceeds asks the user to be more especific.
    if len(message) >= 3:
        for magic in MAG_JSON:
            if unidecode(magic['name']).lower().find(message.lower()) == 0:
                spell_ids.append(magic['id'])
        if len(spell_ids) <= 3:
            return spell_ids
        else:
            await ctx.send("Foram encontradas " + str(len(spell_ids)) + " magias. Por favor seja mais especifico.")   

# Function that creates the embed of the magic based on id.
async def embed_magic(id):

    name = str(MAG_JSON[id]['name'])
    tier = f"***{str(MAG_JSON[id]['tier'])}° Circulo - {str(MAG_JSON[id]['type'])}({str(MAG_JSON[id]['school'])})*** \n \n"

    description = f"{tier} **Execução:** {str(MAG_JSON[id]['execution'])}\n**Alcance:** {str(MAG_JSON[id]['distance'])} \n**{str(MAG_JSON[id]['targetType'])}** {str(MAG_JSON[id]['target'])} \n**Duração:** {str(MAG_JSON[id]['duration'])}"
    
    if MAG_JSON[id]['resistence'] != None:
        description = f'{description} \n **Resistência:** {str(MAG_JSON[id]["resistence"])} \n \n {str(MAG_JSON[id]["description"])}'
    else:
        description = f'{description} \n \n {str(MAG_JSON[id]["description"])}'

    # Magic embed body
    magic = discord.Embed(
    title = name,
    description = description,
    color=discord.Color.random())
    # Set image to be sent with the embed
    magic.set_image(url="attachment://image.jpg")

    if MAG_JSON[id]['extraTitle'] != None:
        x = 0
        while x < len(MAG_JSON[id]['extraTitle']):
            magic.add_field(name=str(MAG_JSON[id]['extraTitle'][x]), value=str(MAG_JSON[id]['extraDesc'][x]), inline=False)
            x = x+1
        return magic
    else:
        return magic