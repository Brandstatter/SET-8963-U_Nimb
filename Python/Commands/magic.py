import discord
import json
from discord.ui import View

async def find_magic(ctx, identity):
    MAG_JSON = json.load(open("json\magics.json", encoding='utf-8'))
    if identity.isnumeric() == True:
        for magic in MAG_JSON:
            if int(identity) == magic['id']:
                await embed_magic(ctx, int(identity))
    else:
        nameMagic = ctx.message.content
        nameMagic = nameMagic[3:]
        for magic in MAG_JSON:
            if magic['name'].lower().find(nameMagic.lower()) == 0:
                id = magic['id']
                await embed_magic(ctx, id)


# Function that creates the embed of the magic based on id.
async def embed_magic(ctx, id):
    # Open .json file that contain the magic data
    MAG_JSON = json.load(open("json\magics.json", encoding='utf-8'))

    # Block of code that pulls specifics data for the embed. (Enconding in latin necessary to accents.)
    name = str(MAG_JSON[id]['name']).encode('latin-1')
    type = str(MAG_JSON[id]['type']).encode('latin-1')
    text = MAG_JSON[id]['tier']
    name = name.decode('latin-1')
    type = type.decode('latin-1')
    
    # Get path to the image from json
    file = discord.File(MAG_JSON[id]['img'][0], filename="image.jpg")
    
    # Magic embed body
    magic = discord.Embed(
    title = name,
    description = str(type) +"\nCirculo: "+ str(text),
    color=discord.Color.random())

    # Set image to be sent with the embed
    magic.set_image(url="attachment://image.jpg")

    if len(MAG_JSON[id]["img"]) > 1:
        prev_button = discord.ui.Button(label = ">", style = discord.ButtonStyle.green, custom_id = 'next')
        next_button = discord.ui.Button(label = "<", style = discord.ButtonStyle.green, custom_id = 'prev')

        global index_img
        index_img = 0

        # FIXME The function to change image is returning an error
        # This still could be improved but focusing on this will only stall progress on the next features.
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
        await ctx.send(file = file, embed = magic)       