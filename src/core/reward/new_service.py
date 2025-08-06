import os
import discord
import json
import random

from core.reward.embeds.embed_money import embed_money
from core.reward.embeds.embed_fail import embed_fail

REWARD_JSON = json.load(open(os.path.join("json", "reward.json"), encoding="utf-8"))
WEALTH_JSON = json.load(open(os.path.join("json", "treasure_reward.json"), encoding="utf-8"))

async def get_treasure(id):
    ndObject = next((obj for obj in REWARD_JSON if obj["nd"] == id), None)
    # d100 = random.randrange(1, 100)
    d100 = 100
    if not ndObject:
        return None

    choseReward = None
    for item in ndObject["reward"]:
        if d100 <= item["cutoff"]:
            choseReward = item
            break

    if(choseReward["description"] == None):
        return embed_fail()  

    if(choseReward["description"].get("wealth") is not None):
        wealthObject = next(( obj for obj in WEALTH_JSON if obj.type == choseReward.wealth.type))

        runD100 = random.randrange(1, 100)
        probabilities = wealthObject.probability
        chosenWealth = None
        for probability in probabilities:
            if(probability.cutoffValue <= runD100):
                chosenWealth = probability
                break
            
        if(chosenWealth == None):
            return None

        solveRolls = 0
        for _ in range(chosenWealth.numberOfRolls):
            solveRolls += (random.randrange(1, chosenWealth.dice) * chosenWealth.bonus) 

        return



    rolledDice = []
    for _ in range(choseReward["description"]["numberOfRolls"]):
        rollDice = random.randrange(1, choseReward["description"]["chosenDie"])
        rolledDice.append(rollDice)

    return embed_money(choseReward=choseReward, rolled_dice=rolledDice, d100=d100)