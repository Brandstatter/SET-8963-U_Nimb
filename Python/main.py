import os

import discord
import random

import Commands.qualityCtrl
import Commands.magic
import Commands.conditions
import Commands.dice
import Commands.generate_attribute

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
async def on_ready() :
    global guilds_list
    guilds_list = [guild.id for guild in client.guilds]
    print("Bot pronto.")

#TODO Add slash commands
#TODO Improve design of the help function

# Slash Commands Section

@client.slash_command(
    name = "help",
    guild_ids = [563153398392684554]
)
async def help(ctx):
    await ctx.respond(f"Ty - Retorna uma magica aleatoria /n Te + Nome de uma magia - Retorna explicação da magia especifica. /n Td + Valor do dado(6, 12, 20) + Numero de Dados + Bonus - Retorna uma magica aleatoria /n Tfeedback - Função para enviar reporte de bugs ou sugestões de melhoria.")

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

@client.slash_command(
        name = "condição",
        description = "Comando para pesquisa de condições.",
        guild_ids = [563153398392684554]
)
async def slash_condition(ctx,
    condtion_option : discord.Option(str, choices = ['Abalado', 'Agarrado', 'Alquebrado', 'Apavorado', 'Atordoado', 'Caído', 'Cego', 'Confuso', 'Debilitado', 'Desprevenido', 'Doente', 'Em Chamas', 'Enjoado', 'Enredado', 'Envenenado', 'Esmorecido', 'Exausto', 'Fascinado', 'Fatigado', 'Fraco', 'Frustrado', 'Imovel', 'Inconsciente', 'Indefeso', 'Lento', 'Ofuscado', 'Paralisado', 'Pasmo', 'Petrificado', 'Sangrando', 'Surdo', 'Surpreendido', 'Vulnerável'])
):
    id = 23
    embed, file = await Commands.conditions.embed_condition(ctx, id)
    await ctx.respond(embed = embed, file = file)


# Prefix Commands Section

# Random Magic
@client.command(aliases = ['y']) 
async def descarte(ctx):
    print("usou descarte")
    embed, file = await Commands.magic.embed_magic(ctx, random.randrange(0, 197))
    print(embed)
    await ctx.send(embed = embed, file = file)

# Search Magic
@client.command(aliases = ['e']) 
async def searchMagic(ctx, name:str):
    id = await Commands.magic.search_magic(ctx, name)
    print(id)
    for magic in id:
        embed, file = await Commands.magic.embed_magic(ctx, magic)
        print(embed)
        await ctx.send(embed = embed, file = file)

# Dice
@client.command(aliases = ['D']) # TODO Improve command
async def dice(ctx, nDice: int, nNumb: int, nBonus: int):
    print("usou dados")
    await Commands.dice.roll_dice(ctx, nDice, nNumb, nBonus)    

@client.command(aliases = ['g'])
async def search_condition(ctx, name:str):
    id = await Commands.conditions.search_condition(ctx, name)
    embed, file = await Commands.conditions.embed_condition(ctx, id)
    if file == None:
        await ctx.send(embed = embed)
    else:
        await ctx.send(embed = embed, file = file)

@client.command()
async def i(ctx): #FIXME
    embed, file = await Commands.magic.embed_magic(ctx, 0)
    await ctx.send(embed = embed, file = file)
    
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