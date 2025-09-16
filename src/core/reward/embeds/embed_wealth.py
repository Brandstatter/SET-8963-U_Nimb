import discord

from core.reward.treasure_enum import TreasureEnum

def embed_wealth(choseReward, treasures, rolls):
    embeds = []
    wealthType = choseReward["description"]["wealth"]["type"]

    embed = discord.Embed(
        title=TreasureEnum.from_code(wealthType),
        description=None,
        color=discord.Color.random() 
    )

    embed.add_field(name="Número de riquezas", value=rolls, inline=False)

    totalSum = 0
    for index, item in enumerate(treasures):
        bonus = item["bonus"]
        totalSum += sum(item["rolls"]) + bonus

        embeds.append(rollsEmbed(index=index, treasure=item))

    
    embed.add_field(name="Total das jogadas + bônus", value=f"{totalSum}", inline=False)
    embeds.append(embed)

    return embeds

def rollsEmbed(index, treasure):
    dice = treasure["dice"]
    numberOfRolls = treasure["numberOfRolls"]
    bonus = treasure["bonus"]
    rolls = treasure["rolls"]
    examples = treasure["examples"]
    
    rollsStr = " + ".join(str(r) for r in rolls)
    examplesString = "\n".join(str(item) for item in examples)

    totalSum = sum(rolls)
    equation = f"d{dice}x{numberOfRolls} -> {rollsStr} = {totalSum} * {bonus} = {totalSum + bonus}" 

    embed = discord.Embed(
        title=f"Jogada: {index + 1}",
        description=f"{equation}",
        color=discord.Color.random()
    )

    embed.add_field(name="Dados lançados", value=rollsStr, inline=False)
    embed.add_field(name="Bônus", value=bonus, inline=False)
    

    embed.add_field(name="Exemplos de prêmios", value=examplesString, inline=False)

    return embed

