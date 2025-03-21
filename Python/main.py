import os
import discord
from discord.ext import commands
from discord.ui import View
import random
import json
from Commands.magic import embed_magic, find_magic
from Commands.dice import roll_dice
from Commands.generate_attribute import attributes
from dotenv import load_dotenv

intents = discord.Intents.all()

activity = discord.Game(name="Thelp")
client = commands.Bot(command_prefix = "T", case_insensitive = True, activity = activity, status = discord.Status.online, intents = intents)

client.remove_command("help")

def configure():
    load_dotenv()

@client.command() 
async def help(ctx):
    await ctx.send('Ainda não existe.')

# Random Magic
@client.command(aliases = ['y']) # WORKING
async def descarte(ctx):
    await embed_magic(ctx, random.randrange(0, 197))

# Search Magic (Kinda)
@client.command(aliases = ['e']) # WORKING
async def teste(ctx, name:str):
    await find_magic(ctx, name)

# Dice
@client.command(aliases = ['D']) # WORKING
async def dice(ctx, nDice: int, nNumb: int, nBonus: int):
    await roll_dice(ctx, nDice, nNumb, nBonus)    

@client.command()
async def i(ctx): #FIXME
    await attributes(ctx)
    

# Test Command
@client.command()
async def T(ctx):
    cond = json.load(open("json\conditions.json"))
    sendTrem = View()
    sendBagulho = View()

    i = 0
    while i < 33:
        print (i)
        name = str(cond[i]['name']).encode('latin-1')
        button = discord.ui.Button(label = name.decode('utf-8'), style = discord.ButtonStyle.green, custom_id = str(i))
        print(button)
        async def call_condition(interaction):
            print("teste")

        button.callback = call_condition
        if i >= 15:
            sendBagulho.add_item(button)
        else:
            sendTrem.add_item(button)
        i += 1

    await ctx.send(view = sendTrem)
    await ctx.send(view  = sendBagulho)


configure()
client.run(os.getenv('clientID'))