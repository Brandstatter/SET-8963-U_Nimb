import discord
import random

async def roll_dice(ctx, dice_value: int, dice_qtd: int, dice_bonus: int):
    if dice_qtd > 50:
        embed = discord.Embed(
        title = f'Quantidade de dados excedida',
        description = f'Esse comando pode rolar apenas 50 dados de uma vez. {dice_qtd} ultrapassa esse limite.',
        color=discord.Color.random())
        return embed
    else:
        result = 0
        dices = []
        dice_index = 0
        while dice_index < dice_qtd:
            num = random.randrange(1, dice_value)
            dices.append(num)
            dice_index += 1
        index_addition = 0
        while index_addition < len(dices):
            result += dices[index_addition]
            index_addition += 1

        embed = discord.Embed(
        title = f'Resultado {result + dice_bonus}',
        description = f'Quantidade de dados: {dice_qtd} \n Tipo de Dado: D{dice_value} \n \n `{str(dices)}` -> `{result} + {str(dice_bonus)} = {result + dice_bonus}`',
        color=discord.Color.random())
        return embed

async def range_roll(ctx, start:int, end:int):
    if end < start:
        resultado = random.randrange(end, start)
        rangeText = f'{end} e {start}'
    elif start - end == 0:
        resultado = start
    else:
        resultado = random.randrange(start, end)
        rangeText = f'{start} e {end}'
    embed = discord.Embed(
    title = f'Rolagem entre {rangeText}',
    description = f' # Resultado: {resultado}',
    color=discord.Color.random())

    return embed