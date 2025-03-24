import discord
import random
from discord.ui import View


# FIXME problem of awaiting function inside loops
async def attributes(ctx):
    # Embed explanation of ways to get atributes
    types_attributes = discord.Embed(title = "Formas para gerar Atributos", color = 15844367)
    
    # Field explaining dice generation method.
    types_attributes.add_field(name = "Geração por Dados", value = "Esse método gera os valores dos atributos por dados. Rodando 4d6 retirando o menor valor e somando o restante e assim repetindo o processo 6 vezes. Com os valores em mãos o jogador escolhe quais valor vai em cada atributo.")

    # Field explaining point buy method.
    types_attributes.add_field(name = "Geração por Pontos", value = "Esse método permite o jogador comprar os atributos que ele quiser. O jogador possui 20 pontos para gastar, caso o custo do atributo seja negativo se ganha pontos, caso o custo for positivo se perde pontos. Os custos e valores dos atributos podem ser vistos na tabela ao selecionar o método.")
    
    # Buttons creation
    dice_button = discord.ui.Button(label = "Dados", style = discord.ButtonStyle.green, custom_id = 'Dice')
    point_buy_button = discord.ui.Button(label = "Pontos", style = discord.ButtonStyle.green, custom_id = 'Points')

    # Callback function for the dice method button.
    async def call_dice(interaction):
        buttons.clear_items()
        await ctx.send(await dices())
        await message.edit(embed = types_attributes, view = buttons)


    # TODO Create Point Version of Attributes
    # Setting callbacks functions.
    dice_button.callback = call_dice

    # Setup View and add buttons to it.
    buttons = View()
    buttons.add_item(point_buy_button)
    buttons.add_item(dice_button)

    message = await ctx.send(embed = types_attributes, view = buttons)

# Starting Dice Method Function
async def dices():
    global FirstIs
    global modList

    FirstIs = True
    modList = []
    dices = []

    # Fully load the attributes list with random values (Based on the game method of generating values)
    j = 0
    while j < 6:
        dices.append(await generate_att())
        j += 1
     
    mod = await calc_mod(dices)
    for i in mod:
        i += i
    while i < 6:
        dices.sort()
        dices = await redo(dices)
        mod = await calc_mod(dices)
        for att in mod:
            i += att

    return dices

# Function that calculate the modifier off the attribute
async def modifier(att):
    match att:
        case 1:
            mod = -5
        case 2 | 3:
            mod = -4
        case 4 | 5:
            mod = -3
        case 6 | 7:
            mod = -2
        case 8 | 9:
            mod = -1
        case 12 | 13:
            mod = 1
        case 14 | 15:
            mod = 2
        case 16 | 17:
            mod = 3
        case 18:
            mod = 4
        case _:
            mod = 0
    return mod

async def generate_att():
    attr = 0
    i = 0
    while i < 3:
        num = random.randrange(1, 6)
        attr += num
        i += 1
    return attr

async def redo(dices: list):
    dices.sort()
    old = dices[0]
    attr = await generate_att()
    if old % 2:
        while attr <= old + 1:
            attr = await generate_att()
    else:
        while attr <= old:
            attr = await generate_att()
    del dices[0]
    dices.append(attr)
    return dices

async def calc_mod(dices):
    # Declare global variables to use in this function.
    global FirstIs
    global modList

    # If is the first iteraction, calculates every attribute
    if FirstIs == True:
        for att in dices:
            modList.append(modifier(att))
            FirstIs = False 
    
    # If isnt the first iteraction, calculate the new attribute modifier
    else:
        # sort and delete the lowest value on modList
        modList.sort()
        del modList[0]

        # Append the new attribute modifier on modList
        modList.append(modifier(dices[5]))
    print(modList)
    return modList