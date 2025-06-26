import discord
import json
import random
import math

MONEY_JSON = json.load(open("json\moneyReward.json", encoding='utf-8'))

# Rolls D100 and get the type of reward relative to index.
async def get_percent(id):
    d100 = random.randrange(1,100)
    percentages = MONEY_JSON[id]['percentages']

    index = 0
    # Check if dice roll is higher than each number on percentages.
    while d100 > percentages[index]:
        index += 1
    # Halfes index and round to the lowest number to get index of the reward.
    index = int(math.floor(index/2))

    """
    Treasure types
    None = No reward.
    0 = Money.
    1 = Small Treasure / 2 = Small Treasure Roll with bonus
    3 = Medium Treasure / 4 = Medium Treasure Roll with bonus
    5 = Medium Treasure / 6 = Big Treasure Roll with bonus
    """
    if MONEY_JSON[id]['treasureType'][index] == 0:
        embed = await get_money(id, d100, index)
        return embed
    elif MONEY_JSON[id]['treasureType'][index] == None:
        embed = await embed_nulo(id, d100)
        return embed
    else:
        embed = await get_treasure(id, index)
        return embed

async def get_money(id, d100, percent):
    dicesQtd = MONEY_JSON[id]['rewardDiceQtd'][percent]
    dicesType = MONEY_JSON[id]['rewardDice'][percent]
    diceBonus = MONEY_JSON[id]['diceBonus'][percent]
    rewardQtd = MONEY_JSON[id]['rewardQtd'][percent]
    
    # Since the Bonus is garanted the starting diceValues for the dices is going to be the bonus, if there's no bonus the diceValues will be 0.
    diceValue = diceBonus
    dices = []
    
    index = 1
    while index <= dicesQtd:
        dice = random.randrange(1, dicesType)
        dices.append(dice)
        diceValue =+ diceValue + (dice)
        index = index+1
    
    result = diceValue*rewardQtd

    embed = await embed_money(id, d100, result, dices)
    return embed
    
async def get_treasure(id, percent):
    embed = await embed_treasure(id, 100, 13, [1,4])
    return embed

async def embed_money(id, d100, result, dices):
    title = f'Recompensa ND : {MONEY_JSON[id]["ND"]}'
    desc = f'## Resultado : {result} \n D100: {d100}\n TABELA \nTABELA \nTABELA \nTABELA \n \n D100: sla \n Dados rolados : `{dices}`'

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