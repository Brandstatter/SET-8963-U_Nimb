import os

import random
import json

from discord.commands import Option
from discord.ui import View  
from dotenv import load_dotenv
from clientConfig import client

import core.sync.command
import core.reward.command
import core.conditions.command
import core.dice.comand
import core.magic.command
import core.origins.command
import core.quality.command
import core.race.command
import core.reward.command
import core.help.command
import core.itens.command
import core.equipament.command
import core.magic_accessories.command
import core.chaos_cards.command
import core.potions.command

def configure():
    load_dotenv()

json_path = os.path.join("json", "guilds.json")
GUILDS_JSON = json.load(open(json_path, encoding='utf-8'))
global guilds_list
guilds_list = GUILDS_JSON[0]['guilds']

@client.event
async def on_ready() :
    await client.sync_commands()
    guilds_ = [guild.id for guild in client.guilds]
    print (guilds_)
    print("Bot pronto. ")

@client.event
async def on_guild_join(guild):
    with open(json_path, 'r') as file:
        data = json.load(file)
        
    data[0]['guilds'].append(guild.id)
    with open(json_path, 'w') as outputFile:
        json.dump(data, outputFile, indent=4)

@client.event
async def on_guild_remove(guild):
    with open(json_path, 'r') as file:
        data = json.load(file)
    data[0]['guilds'].remove(guild.id)
    with open(json_path, 'w') as outputFile:
        json.dump(data, outputFile, indent=4)


   
configure()
client.run(os.getenv('clientID'))