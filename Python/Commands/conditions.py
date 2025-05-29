import discord
import json

from unidecode import unidecode


COND_JSON = json.load(open("json\conditions.json", encoding='utf-8'))

listCond = []
for cond in COND_JSON:
    listCond.append(cond['name'])
print(listCond)


async def search_condition(ctx, id):
    message = unidecode(ctx.message.content)
    # Remove prefix from message content
    message = message[6:]
    list_ids = []
    if len(message) >= 4:
        print(message.lower())
        for condition in COND_JSON:
            print(condition['name'].lower())
            if unidecode(condition['name']).lower().find(message.lower()) == 0:
                list_ids.append(condition['id'])
        if len(list_ids) == 1:
            return list_ids[0]
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
    file = None
    if COND_JSON[id]['img'] != None:
        file = discord.File(COND_JSON[id]['img'], filename="image.jpg")

    # Conditions embed body
    conditions = discord.Embed(
    title = name.decode('latin-1'),
    description = type_cond.decode('latin-1'),
    color = discord.Color.random())
    
    # Work around subtext existence or not
    if subtext == None:
        conditions.add_field(name="Efeitos", value= text.decode('latin-1'), inline=False)
    else:
        subtext = subtext.decode('latin-1')
        conditions.add_field(name="Efeitos", value= text.decode('latin-1') + '\n' + str(subtext), inline=False)
    
    # Set image to be sent with the embed
    conditions.set_image(url="attachment://image.jpg")
    
    return conditions, file