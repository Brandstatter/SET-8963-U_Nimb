import discord
import json

from unidecode import unidecode


COND_JSON = json.load(open("json\conditions.json"))

async def search_condition(ctx, id):
    if id.isnumeric() == True:
        for condition in COND_JSON:
            if int(id) == condition['id']:
                await embed_condition(ctx, int(id))
    else:
        message = unidecode(ctx.message.content)
        message = message[3:]
        list_ids = []
        if len(message) >= 4:
            for condition in COND_JSON:
                # FIXME  Caido changes to CaAdo and vulneravel changes to VulnerA!vel
                if unidecode(condition['name']).lower().find(message.lower()) == 0:
                    list_ids.append(condition['id'])
            if len(list_ids) == 1:
                for id in list_ids:
                    await embed_condition(ctx, id)
            else:
                await ctx.send("Encontramos " + str(len(list_ids)) + " condições, por favor seja mais específico.")


# Function that creates the embed of the condition based on id.
async def embed_condition(ctx, id):
    # Block of code that pulls specifics data for the embed. (Enconding in latin necessary to accents.)
    name = str(COND_JSON[id]['name']).encode('latin-1')
    type_cond = str(COND_JSON[id]['typeC']).encode('latin-1')
    text = str(COND_JSON[id]['text']).encode('latin-1')
    subtext = str(COND_JSON[id]['subtext']).encode('latin-1')
    # Get path to the image from json
    file = discord.File(COND_JSON[id]['img'], filename="image.jpg")
        
    # Conditions embed body
    conditions = discord.Embed(
    title = name.decode('utf-8'),
    description = type_cond.decode('utf-8'),
    color = discord.Color.random())
    
    # Work around subtext existence or not
    if subtext == None:
        # If theres no subtext, only the main text is added
        conditions.add_field(name="Efeitos", value= text.decode('utf-8'), inline=False)
    else:
        # If theres a subtext, will decode and ad on field
        subtext = subtext.decode('utf-8')
        conditions.add_field(name="Efeitos", value= text.decode('utf-8') + '\n' + str(subtext), inline=False)
    
    # Set image to be sent with the embed
    conditions.set_image(url="attachment://image.jpg")

    await ctx.send(file = file, embed = conditions)