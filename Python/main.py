import os

import discord
import random
import json

import Commands.help
import Commands.qualityCtrl
import Commands.magic
import Commands.conditions
import Commands.dice
import Commands.race

from discord.ext import commands
from discord import SlashCommandGroup
from discord.ui import View
from dotenv import load_dotenv


intents = discord.Intents.all()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.listening, name="Prefixo 'T'")
client = commands.Bot(command_prefix = "T", case_insensitive = True, activity = activity, status = discord.Status.online, intents = intents)

client.remove_command("help")

def configure():
    load_dotenv()

@client.event
async def on_guild_join(guild):
    with open("json\guilds.json", 'r') as file:
        data = json.load(file)
        
    data[0]['guilds'].append(guild.id)
    with open("json\guilds.json", 'w') as outputFile:
        json.dump(data, outputFile, indent=4)

#TODO Add slash commands
#TODO Improve design of the help function

# Slash Commands Section

@client.slash_command(
    name = "help",
    guild_ids = [563153398392684554, 474008663174938637]
)
async def help(ctx):
    user = await ctx.user.create_dm()
    await ctx.respond("Comandos enviados para sua DM!")
    await user.send(embed = await Commands.help.embed_help())

@client.slash_command(
    name = "races",
    description = "Retorna atributos e habilidades da raça selecionada.",
    guild_ids = [563153398392684554]
)
async def slash_race(ctx,
    race_option : discord.Option(str, choices = ['Humano', 'Anão', 'Dahllan', 'Elfo', 'Goblin', 'Lefou', 'Minotauro', 'Qareen', 'Golem', 'Hynne', 'Kliren', 'Medusa', 'Osteon', 'Sereia/Tritão', 'Sílfide', 'Suraggel', 'Trog'])
):
    id = await Commands.race.switcher_race(race_option)
    embed = await Commands.race.embed_race(ctx, id)
    await ctx.respond(embed = embed)

@client.slash_command(
    name = "feedback",
    description = "Comando para sugerir melhorias, novas features ou reportar bugs no bot.",
    guild_ids = [563153398392684554]
)
async def slash_feedback(ctx, 
    feedback_option : discord.Option(str, choices = ["Feature", "Bug", "Sugestão"])
    ):
    original_author = ctx.author
    if feedback_option == "Feature":
        await ctx.respond("Por favor escreva qual a feature você gostaria que fosse adicionado no Magic Madness. Não esqueça de descrever oque a feature deve realizar.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await Commands.qualityCtrl.feature(msg)
    elif feedback_option == "Bug":
        await ctx.respond("Por favor informe qual o comando que o bug se encontra e descreva oque está acontecendo.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await Commands.qualityCtrl.bug(msg)
    else:
        await ctx.respond("Por favor informe o comando e como podemos melhorar a sua experiencia.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await Commands.qualityCtrl.suggestion(msg)

# Prefix Commands Section

# Random Magic
@client.command(aliases = ['l', 'random']) 
async def randomMagic(ctx):
    embed, file = await Commands.magic.embed_magic(ctx, random.randrange(0, 197))
    await ctx.send(embed = embed, file = file)

# Search Magic
@client.command(aliases = ['e', 'magia']) 
async def searchMagic(ctx, name:str):
    id = await Commands.magic.search_magic(ctx, name)
    for magic in id:
        embed, file = await Commands.magic.embed_magic(ctx, magic)
        print(embed)
        await ctx.send(embed = embed, file = file)

# Dice
@client.command(aliases = ['D']) # TODO Improve command
async def dice(ctx, nDice: int, nNumb: int, nBonus: int):
    print("usou dados")
    await Commands.dice.roll_dice(ctx, nDice, nNumb, nBonus)    

@client.command(aliases = ['cond'])
async def search_condition(ctx, name:str):
    id = await Commands.conditions.search_condition(ctx, name)
    embed, file = await Commands.conditions.embed_condition(ctx, id)
    if file == None:
        await ctx.send(embed = embed)
    else:
        await ctx.send(embed = embed, file = file)

# Consult info about different races from the game
@client.command(aliases = ['r','raças', 'races'])
async def search_races(ctx): 
    await Commands.race.search_race(ctx)
    
# Give user option to report bugs or send ideas to new features
@client.command(aliases = ['t', 'report'])
async def feedback(ctx):
    #TODO Remove buttons after being clicked
    original_author = ctx.message.author

    await ctx.send("Obrigado por nos ajudar a melhorar o Magic Madness!")
    await ctx.send("Deseja sugerir uma feature nova, reportar um bug ou dar uma sugestão de melhoria?")
    feedback_button = discord.ui.Button(label = "Feedback", style = discord.ButtonStyle.green, custom_id = 'Feedback')
    bug_button = discord.ui.Button(label = "Bug", style = discord.ButtonStyle.red, custom_id = 'Bug')
    feature_button = discord.ui.Button(label = "Feature", style = discord.ButtonStyle.green, custom_id = 'Feature')

    buttons = View()

    async def feature_ideia(self):
        await ctx.send("Por favor escreva qual a feature você gostaria que fosse adicionado no Magic Madness. Não esqueça de descrever oque a feature deve realizar.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await Commands.qualityCtrl.feature(msg)

    async def bug_report(self):
        await ctx.send("Por favor informe qual o comando que o bug se encontra e descreva oque está acontecendo.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await Commands.qualityCtrl.bug(msg)
    
    async def feedback(self):
        await ctx.send("Por favor informe o comando e como podemos melhorar a sua experiencia.")
        msg = await client.wait_for("message")
        if original_author == msg.author:
            await Commands.qualityCtrl.suggestion(msg)

    feature_button.callback = feature_ideia
    bug_button.callback = bug_report
    feedback_button.callback = feedback

    buttons.add_item(feature_button)
    buttons.add_item(bug_button)
    buttons.add_item(feedback_button)
    await ctx.send(view = buttons)

@client.command()
async def i(ctx):
    with open("json\guilds.json", 'r') as file:
        data = json.load(file)
        
    data[0]['guilds'].append(31231234354354365)
    with open("json\guilds.json", 'w') as outputFile:
        json.dump(data, outputFile, indent=4)

@client.event
async def on_ready() :
    global guilds_list
    guilds_list = [guild.id for guild in client.guilds]
    print (guilds_list)
    print("Bot pronto.")
   
configure()
client.run(os.getenv('clientID'))