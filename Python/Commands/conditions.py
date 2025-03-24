import discord
import json


# Function that creates the embed of the condition based on id.
async def condition(ctx, x): 
    # Open .json file that contain the conditions data
    COND_JSON = json.load(open("json\conditions.json"))
    
    # Block of code that pulls specifics data for the embed. (Enconding in latin necessary to accents.)
    name = str(COND_JSON[x]['name']).encode('latin-1')
    type_cond = str(COND_JSON[x]['typeC']).encode('latin-1')
    text = str(COND_JSON[x]['text']).encode('latin-1')
    subtext = str(COND_JSON[x]['subtext']).encode('latin-1')
    
    # Get path to the image from json
    file = discord.File(COND_JSON[x]['img'], filename="image.jpg")
        
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