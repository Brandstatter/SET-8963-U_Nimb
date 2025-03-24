import os

import discord
import random

import Commands.qualityCtrl
import Commands.magic
import Commands.conditions
import Commands.dice
import Commands.generate_attribute

from discord.ext import commands
from discord.ui import View
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.listening, name="Prefixo 'T'")
client = commands.Bot(command_prefix = "T", case_insensitive = True, activity = activity, status = discord.Status.online, intents = intents)

client.remove_command("help")

def configure():
    load_dotenv()

#TODO Improve design of the help function
@client.command() 
async def help(ctx):
    await ctx.send('Ty - Retorna uma magica aleatoria')
    await ctx.send('Te + Nome de uma magia - Retorna explicação da magia especifica.')
    await ctx.send('Td + Valor do dado(6, 12, 20) + Numero de Dados + Bonus - Retorna uma magica aleatoria')
    await ctx.send('Tfeedback - Função para enviar reporte de bugs ou sugestões de melhoria.')

#TODO Add slash commands

# Random Magic
@client.command(aliases = ['y']) # WORKING
async def descarte(ctx):
    await Commands.magic.embed_magic(ctx, random.randrange(0, 197))

# Search Magic
@client.command(aliases = ['e']) # WORKING
async def searchMagic(ctx, name:str):
    await Commands.magic.find_magic(ctx, name)

# Dice
@client.command(aliases = ['D']) # TODO Improve command
async def dice(ctx, nDice: int, nNumb: int, nBonus: int):
    await Commands.dice.roll_dice(ctx, nDice, nNumb, nBonus)    

@client.command(aliases = ['g'])
async def search_condition(ctx, name:str):
    await Commands.conditions.search_condition(ctx, name)

@client.command()
async def i(ctx): #FIXME
    await Commands.generate_attribute.attributes(ctx)
    
# Feedback command
@client.command(aliases = ['t'])
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
    
configure()
client.run(os.getenv('clientID'))