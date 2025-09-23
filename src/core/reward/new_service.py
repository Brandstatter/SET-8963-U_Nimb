import os
import json
import random

from core.reward.embeds.embed_wealth import embed_wealth
from core.reward.embeds.embed_money import embed_money
from core.reward.embeds.embed_fail import embed_fail

REWARD_JSON = json.load(open(os.path.join("json", "reward.json"), encoding="utf-8"))
WEALTH_JSON = json.load(open(os.path.join("json", "treasureReward.json"), encoding="utf-8"))

async def get_treasure(id):
    ndObject = next((obj for obj in REWARD_JSON if obj["nd"] == id), None)
    d100Main = random.randrange(1, 100)
    if not ndObject:
        return embed_fail()

    choseReward = None
    for item in ndObject["reward"]:
        if d100Main <= item["cutoff"]:
            choseReward = item
            break

    if(choseReward["description"] == None):
        return embed_fail()  

    if(choseReward["description"].get("wealth") is not None):
        wealthRolls = roll_number_of_wealth(choseReward=choseReward)
        wealthReward = 0
        treasures = []
        for _ in range(wealthRolls):
            treasureSelected = get_selected_wealth(choseReward=choseReward)
            d100Wealth = random.randrange(1, 100)
            if choseReward["description"]["wealth"].get("incentive") is not None:
                d100Wealth = min(100, int(d100Wealth * 1.2))

            treasure = None
            for item in treasureSelected["probability"]:
                if d100Wealth <= item["cutoffValue"]:
                    treasure = item
                    break

            if(treasure == None):
                return embed_fail()

            treasures.append(treasure)

        for item in treasures:
            dice = item["dice"]
            numberOfRolls = item["numberOfRolls"]

            rolls = []
            for _ in range(numberOfRolls):
                wealthValue = random.randrange(1, dice)
                wealthReward += wealthValue
                
                rolls.append(wealthValue)

            item["rolls"] = rolls
    
        return embed_wealth(choseReward=choseReward, treasures=treasures, rolls=wealthRolls, d100Main=d100Main, d100Wealth=d100Wealth)


    rolledDice = []
    for _ in range(choseReward["description"]["numberOfRolls"]):
        rollDice = random.randrange(1, choseReward["description"]["chosenDie"])
        rolledDice.append(rollDice)

    return embed_money(choseReward=choseReward, rolled_dice=rolledDice, d100=d100Main)


def roll_number_of_wealth(choseReward):
    numberOfRolls = choseReward["description"]["numberOfRolls"]
    chosenDie = choseReward["description"]["chosenDie"]
    bonus = choseReward["description"]["wealth"]["bonus"]

    wealth_rolls = 0
    for _ in range(numberOfRolls):

        wealth_rolls += random.randint(1, chosenDie)

    return wealth_rolls + bonus

def get_selected_wealth(choseReward):
    wealthType = choseReward["description"]["wealth"]["type"]
    return next((obj for obj in WEALTH_JSON if obj["type"] == wealthType), None)
    
