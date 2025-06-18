import discord
import json
import random
import math
import asyncio

MONEY_JSON = json.load(open("json\moneyReward.json", encoding='utf-8'))

async def get_percent(id):
    d100 = random.randrange(1,100)
    percentages = MONEY_JSON[id]['percentages']
    x = 0
    while d100 > percentages[x]:
        x += 1
    final = int(math.floor(x/2))
    if MONEY_JSON[id]['treasureType'][final] == 0:
        embed = await get_money(id, final)
        return embed
    elif MONEY_JSON[id]['treasureType'][final] == None:
        embed = await embed_nulo(id, d100)
        return embed
    else:
        print("tesouro")
        embed = await get_treasure(id, final)
        return embed



async def get_money(id, percent):
    dicesQtd = MONEY_JSON[id]['rewardDiceQtd'][percent]
    dicesType = MONEY_JSON[id]['rewardDice'][percent]
    diceBonus = MONEY_JSON[id]['diceBonus'][percent]
    rewardQtd = MONEY_JSON[id]['rewardQtd'][percent]
    
    # Since the Bonus is garanted the starting diceValues for the dices is going to be the bonus, if there's no bonus the diceValues will be 0.
    diceValue = diceBonus
    dices = []
    
    x = 1
    while x <= dicesQtd:
        dice = random.randrange(1, dicesType)
        dices.append(dice)
        diceValue =+ diceValue + (dice)
        x = x+1
    
    result = diceValue*rewardQtd

    embed = await embed_money(id, percent, result, dices)
    return embed
    
async def get_treasure(id, percent):
    embed = await embed_treasure(id, 100, 13, [1,4])
    return embed

async def embed_money(id, d100, result, dices):
    title = f'Recompensa ND : {MONEY_JSON[id]["ND"]}'
    desc = f'## Resultado : {result} \n TABELA \nTABELA \nTABELA \nTABELA \n \n D100: sla \n Dados rolados : {dices}'

    reward = discord.Embed(
        title = title,
        description = desc,
        color=discord.Color.gold()
    )
    
    return reward

async def embed_nulo(id, dado):
    title = f'Recompensa ND : {MONEY_JSON[id]["ND"]}'
    desc = f'## Sem Recompensa \n D100: {dado} \n TABELA \n TABELA \n TABELA \n TABELA \n'

    reward = discord.Embed(
        title= title,
        description= desc,
        color= discord.Color.darker_grey()
    )

    return reward

async def embed_treasure(id, d100, result, dices):
    title = f'Recompensa ND : {MONEY_JSON[id]["ND"]}'
    desc = f'## Resultado : riqueza \n TABELA \nTABELA \nTABELA \nTABELA \n \n D100: sla \n Dados rolados : {dices}'

    reward = discord.Embed(
        title = title,
        description = desc,
        color=discord.Color.gold()
    )
    
    return reward