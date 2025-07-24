import os
import discord
import json
import random
import math

moneyJsonPath = os.path.join("json", "moneyReward.json")
treasureJsonPath = os.path.join("json", "moneyReward.json")

MONEY_JSON = json.load(open(moneyJsonPath, encoding='utf-8'))
TREASURE_JSON = json.load(open(treasureJsonPath, encoding='utf-8'))

MONEYCOPY_JSON = json.load(open(os.path.join("json", "moneyRewardCopy.json"), encoding="utf-8"))

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
    if MONEY_JSON[id]['treasureType'][index] == 0:
        embed = await get_money(id, d100, index)
        return embed
    elif MONEY_JSON[id]['treasureType'][index] == None:
        embed = await embed_nulo(id, d100)
        return embed
    else:
        embed = await get_treasure(id, d100, index)
        return embed

async def get_money(id, d100, index_reward):
    # Since the Bonus is garanted the starting diceValues for the dices is going to be the bonus, if there's no bonus the diceValues will be 0.
    diceValue = MONEY_JSON[id]['diceBonus'][index_reward]
    dices = []
    
    index = 1
    while index <= MONEY_JSON[id]['rewardDiceQtd'][index_reward]:
        dice = random.randrange(1, MONEY_JSON[id]['rewardDice'][index_reward])
        dices.append(dice)
        diceValue =+ diceValue + (dice)
        index = index+1

    if MONEY_JSON[id]["diceBonus"][index_reward] != 0:
        dices = f'`{dices} + {MONEY_JSON[id]["diceBonus"][index_reward]} = {diceValue}`'
    else:
        dices = f'`{dices} = {diceValue}`'

    result = diceValue*MONEY_JSON[id]['rewardQtd'][index_reward]

    embed = await embed_money(id, d100, result, dices, index_reward)
    return embed
    
async def get_treasure(id, d100, index):
    d100_list = []
    values_list = []
    if MONEY_JSON[id]['rewardDice'][index] == 1:
        treasure_quantity = 1
    else:
        treasure_quantity = random.randrange(1, MONEY_JSON[id]['rewardDice'][index]) 
    treasure_quantity = treasure_quantity + MONEY_JSON[id]['diceBonus'][index]
    x = 0
    while x < treasure_quantity:
        d100_treasure = random.randrange(1, 100)
        if MONEY_JSON[id]['treasureType'][index] % 2 == 0:
            if d100_treasure >= 70:
                d100_treasure = 100
            else:
                d100_treasure = d100_treasure + 20
        d100_list.append(d100_treasure)
        x = x + 1


    if MONEY_JSON[id]['treasureType'][index] == 1 or MONEY_JSON[id]['treasureType'][index]  == 2:
        total_value = 0
        for y in d100_list:
            new_value = await treasure_value(y , 0)
            values_list.append(new_value)
            total_value  = total_value + new_value

    elif MONEY_JSON[id]['treasureType'][index] == 3 or MONEY_JSON[id]['treasureType'][index]  == 4:
        total_value = 0
        for y in d100_list:
            new_value = await treasure_value(y , 1)
            values_list.append(new_value)
            total_value  = total_value + new_value 
    else:
        total_value = 0
        for y in d100_list:
            new_value = await treasure_value(y , 2)
            values_list.append(new_value)
            total_value  = total_value + new_value  

    embed = await embed_treasure(id, d100, total_value, values_list, index)
    return embed

async def treasure_value(d100Treasure, treasure):
    percentages = TREASURE_JSON[treasure]['percentages']
    
    index_percent = 0
    while d100Treasure > percentages[index_percent]:
        index_percent += 1
    index_percent = int(math.floor(index_percent/2))

    index = 1
    diceValue = 0
    while index <= TREASURE_JSON[treasure]['diceQtd'][index_percent]:
        dice = random.randrange(1, TREASURE_JSON[treasure]['diceType'][index_percent])
        diceValue =+ diceValue + (dice)
        index = index+1

    if TREASURE_JSON[treasure]['currencyMult'][index_percent] != 0:
        diceValue = diceValue * TREASURE_JSON[treasure]['currencyMult'][index_percent]

    return diceValue

# FINISHED
async def embed_money(id, d100, result, dices, index):
    if MONEY_JSON[id]["diceBonus"][index] != 0:
        title = f'Recompensa(ND {MONEY_JSON[id]["ND"]}): {MONEY_JSON[id]["rewardDiceQtd"][index]}D{MONEY_JSON[id]["rewardDice"][index]}+{MONEY_JSON[id]["diceBonus"][index]} x {MONEY_JSON[id]["rewardQtd"][index]}{MONEY_JSON[id]["rewardCurrency"][index]}'
    else:
        title = f'Recompensa(ND {MONEY_JSON[id]["ND"]}): {MONEY_JSON[id]["rewardDiceQtd"][index]}D{MONEY_JSON[id]["rewardDice"][index]} x {MONEY_JSON[id]["rewardQtd"][index]}{MONEY_JSON[id]["rewardCurrency"][index]}'
    
    desc = f'## Resultado: {MONEY_JSON[id]["rewardCurrency"][index]}{result} \n ### **D100: *{d100}***\n Dados rolados : `{dices}`'

    reward = discord.Embed(
        title = title,
        description = desc,
        color=discord.Color.gold()
    )
    reward.set_image(url = MONEY_JSON[id]["link"])
    
    return reward

# FINISHED
async def embed_nulo(id, d100):
    title = f'Recompensa(ND {MONEY_JSON[id]["ND"]})'
    desc = f'## Não encontrou nenhuma recompensa. \n ### **D100: *{d100}***'

    reward = discord.Embed(
        title= title,
        description= desc,
        color= discord.Color.darker_grey()
    )
    reward.set_image(url = MONEY_JSON[id]["link"])

    return reward

async def embed_treasure(id, d100, reward, values, index):
    if MONEY_JSON[id]["rewardDice"][index] != 1:
        if MONEY_JSON[id]["diceBonus"][index] == 0:
            title = f'Recompensa(ND {MONEY_JSON[id]["ND"]}): {MONEY_JSON[id]["rewardDiceQtd"][index]}D{MONEY_JSON[id]["rewardDice"][index]} {MONEY_JSON[id]["rewardCurrency"][index]}'
        else:
            title = f'Recompensa(ND {MONEY_JSON[id]["ND"]}): {MONEY_JSON[id]["rewardDiceQtd"][index]}D{MONEY_JSON[id]["rewardDice"][index]}+{MONEY_JSON[id]["diceBonus"][index]} {MONEY_JSON[id]["rewardCurrency"][index]}'
    else:
        title = f'Recompensa(ND {MONEY_JSON[id]["ND"]}): {MONEY_JSON[id]["rewardDice"][index]} {MONEY_JSON[id]["rewardCurrency"][index]}'
    desc = f'## Recompensa: T${reward} \n ### **D100: *{d100}*** \n Quantidade de riquezas: {str(len(values))} \n Valores das riquezas: {values}'

    reward = discord.Embed(
        title = title,
        description = desc,
        color=discord.Color.gold()
    )
    reward.set_image(url = MONEY_JSON[id]["link"])
    return reward

async def get_treasure(id):
    ndObject = next((obj for obj in MONEYCOPY_JSON if obj["nd"] == id), None)
    d100 = random.randrange(1, 100)
    if not ndObject:
        return None

    money_dict = ndObject["money"]
    choseReward = None
    keys = sorted(int(k) for k in money_dict.keys())
    for k in keys:
        if d100 <= k:
            choseReward = money_dict[str(k)]
            break

    if(choseReward == None):
        print("Sem premio para você")
        return None

    mathSolve = 0
    for i in range(choseReward["numberOfRolls"]):
        rollDice = random.randrange(1, choseReward["chosenDie"])
        print("rollDice", rollDice)
        print("Numero tentativa", i)
        mathSolve = mathSolve + rollDice

    mathSolve = mathSolve * choseReward["multiplier"]

    # print("D100 Escolhido: ", d100)
    # print("Objeto Escolhido: ", choseReward)
    # print("Calculo dos dados resolvidos: ", mathSolve)


    