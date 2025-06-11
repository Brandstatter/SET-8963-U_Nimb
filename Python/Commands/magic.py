""" Functions related with spells part of the Magic Madness bot.

Both functions that create the embeded view of a spell based on the id and the de function to search magic are on this module.
"""

import discord
import json
from unidecode import unidecode
from discord.ui import View


MAG_JSON = json.load(open("json\magics.json", encoding='utf-8'))


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
async def embed_magic(ctx, id):
    # Block of code that pulls specifics data for the embed. (Enconding in latin necessary to portuguese.)
    name = str(MAG_JSON[id]['name'])
    tier = f"***{str(MAG_JSON[id]['tier'])}° Circulo - {str(MAG_JSON[id]['type'])}({str(MAG_JSON[id]['school'])})*** \n \n"
    if str(MAG_JSON[id]['targetType']) == 1:
        target = "**Área:**"
    else:
        target = "**Alvo:**"

    description = f"{tier} **Execução:** {str(MAG_JSON[id]['execution'])}\n**Alcance:** {str(MAG_JSON[id]['distance'])} \n{target} {str(MAG_JSON[id]['target'])} \n**Duração:** {str(MAG_JSON[id]['duration'])}"
    
    if MAG_JSON[id]['resistence'] != None:
        description = f'{description} \n **Resistência:** {str(MAG_JSON[id]["resistence"])} \n \n {str(MAG_JSON[id]["description"])}'
    else:
        description = f'{description} \n \n {str(MAG_JSON[id]["description"])}'

    # Get path to the image from json
    file = discord.File(MAG_JSON[id]['img'][0], filename="image.jpg")
    
    # Magic embed body
    magic = discord.Embed(
    title = name,
    description = description,
    color=discord.Color.random())
    print(type(description))
    # Set image to be sent with the embed
    magic.set_image(url="attachment://image.jpg")

    if len(MAG_JSON[id]["img"]) > 1:
        prev_button = discord.ui.Button(label = ">", style = discord.ButtonStyle.green, custom_id = 'next')
        next_button = discord.ui.Button(label = "<", style = discord.ButtonStyle.green, custom_id = 'prev')

        global index_img
        index_img = 0

        # FIXME The function to change image is returning an error. 
        async def next_pic(interaction):
            global index_img
            if index_img == len(MAG_JSON[id]["img"]) - 1:
                index_img = 0
                file = discord.File(MAG_JSON[id]['img'][index_img], filename="image.jpg")
                magic.set_image(url="attachment://image.jpg")
                await message.edit(file = file, embed = magic)
            else:
                index_img += 1
                file = discord.File(MAG_JSON[id]['img'][index_img], filename="image.jpg")
                magic.set_image(url="attachment://image.jpg")
                await message.edit(file = file, embed = magic)

        async def prev_pic(interaction):
            global index_img
            if index_img == 0:
                index_img = len(MAG_JSON[id]["img"]) - 1
                file = discord.File(MAG_JSON[id]['img'][index_img], filename="image.jpg")
                magic.set_image(url="attachment://image.jpg")
                await message.edit(embed = magic)
            else:
                index_img -= 1
                file = discord.File(MAG_JSON[id]['img'][index_img], filename="image.jpg")
                magic.set_image(url="attachment://image.jpg")
                await message.edit(embed = magic)            
        
        prev_button.callback = next_pic
        next_button.callback = prev_pic
        buttons = View()
        buttons.add_item(next_button)
        buttons.add_item(prev_button)
        message = await ctx.send(file = file, embed = magic, view = buttons)
    else:
        return magic, file      