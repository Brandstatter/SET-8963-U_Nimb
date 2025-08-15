import discord

def embed_wealth(choseReward, treasures):
    numberOfRolls = choseReward["description"]["numberOfRolls"] 
    chosenDie = choseReward["description"]["chosenDie"]
    wealthType = choseReward["description"]["wealth"]["type"]


    embed = discord.Embed(
        title="Prêmio",
        description="Wip"
    )

    print("treasures: ", treasures)
    totalSum = 0
    for index, item in enumerate(treasures):
        bonus = item["bonus"]
        totalSum += sum(item["rolls"]) + bonus


        rollsStr = " + ".join(str(r) for r in item["rolls"])
        equation = f"{rollsStr} + {bonus}" 
        embed.add_field(
            name=str(index),
            value=equation,
            inline=False
        )
    

    return embed
