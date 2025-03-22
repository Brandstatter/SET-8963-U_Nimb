import os
import discord
from discord.ext import commands
from discord.ui import View
import random
import Commands.qualityCtrl
from Commands.magic import embed_magic, find_magic
from Commands.dice import roll_dice
from Commands.generate_attribute import attributes
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.message_content = True

activity = discord.Game(name="Thelp")
client = commands.Bot(command_prefix = "T", case_insensitive = True, activity = activity, status = discord.Status.online, intents = intents)

client.remove_command("help")

def configure():
    load_dotenv()

@client.command() 
async def help(ctx):
    await ctx.send('Ty - Retorna uma magica aleatoria')
    await ctx.send('Te + Nome de uma magia - Retorna explicação da magia especifica.')
    await ctx.send('Td + Valor do dado(6, 12, 20) + Numero de Dados + Bonus - Retorna uma magica aleatoria')
    await ctx.send('Tfeedback - Função para enviar reporte de bugs ou sugestões de melhoria.')

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
    
# Feedback command
@client.command(aliases = ['t'])
async def Feedback(ctx):
    await ctx.send("Obrigado por nos ajudar a melhorar o Magic Madness!")
    await ctx.send("Deseja sugerir uma feature nova, reportar um bug ou dar uma sugestão de melhoria?")
    feedbackButton = discord.ui.Button(label = "Feedback", style = discord.ButtonStyle.green, custom_id = 'Feedback')
    bugButton = discord.ui.Button(label = "Bug", style = discord.ButtonStyle.red, custom_id = 'Bug')
    featureButton = discord.ui.Button(label = "Feature", style = discord.ButtonStyle.green, custom_id = 'Feature')

    buttons = View()

    async def featureIdeia(self):
        await ctx.send("Por favor escreva qual a feature você gostaria que fosse adicionado no Magic Madness. Não esqueça de descrever oque a feature deve realizar.")
        msg = await client.wait_for("message")
        await Commands.qualityCtrl.feature(msg)

    async def bugReport(self):
        await ctx.send("Por favor informe qual o comando que o bug se encontra e descreva oque está acontecendo.")
        msg = await client.wait_for("message")
        await Commands.qualityCtrl.bug(msg)
    
    async def feedback(self):
        await ctx.send("Por favor informe o comando e como podemos melhorar a sua experiencia.")
        msg = await client.wait_for("message")
        await Commands.qualityCtrl.suggestion(msg)

    featureButton.callback = featureIdeia
    bugButton.callback = bugReport
    feedbackButton.callback = feedback

    buttons.add_item(featureButton)
    buttons.add_item(bugButton)
    buttons.add_item(feedbackButton)
    await ctx.send(view = buttons)
    
configure()
client.run(os.getenv('clientID'))