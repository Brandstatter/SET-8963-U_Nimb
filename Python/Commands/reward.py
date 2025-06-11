import discord
import json
import random
import math
import asyncio

MONEY_JSON = json.load(open("json\moneyReward.json", encoding='utf-8'))

async def getPercent(id, dice):
    percentages = MONEY_JSON[id]['percentages']
    print("dados " + str(dice))
    print("% " + str(percentages))
    x = 0
    while dice > percentages[x]:
        x += 1
    #final = int(math.ceil((x-1)/2))
    final = int(math.floor(x/2))
    if MONEY_JSON[id]['isMoney'][final] == True:
        await getMoney(id, final)
    elif MONEY_JSON[id]['isMoney'][final] == None:
        return "Nulo"
    else:
        await getTreasure(id, final)


async def getMoney(id, percent):
    dicesQtd = MONEY_JSON[id]['rewardDiceQtd'][percent]
    dicesType = MONEY_JSON[id]['rewardDice'][percent]
    rewardQtd = MONEY_JSON[id]['rewardQtd'][percent]
    x = 1
    value = 0
    dices = []
    while x <= dicesQtd:
        dice = random.randrange(1, dicesType)
        dices.append(dice)
        value =+ value + (dice*rewardQtd)
        print(value)
        x = x+1
    print(dices)
    print(value)
    
async def getTreasure(id, percent):
    print("Treasure")

print(asyncio.run(getPercent(2, 95)))
#print(asyncio.run(getPercent(3, random.randrange(1, 100))))