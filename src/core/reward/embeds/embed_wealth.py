import discord

from core.reward.treasure_enum import TreasureEnum

def embed_wealth(choseReward, treasures, rolls):
    wealthType = choseReward["description"]["wealth"]["type"]

    embed = discord.Embed(
        title=TreasureEnum.from_code(wealthType),
        description=None,
        color=discord.Color.random() 
    )

    embed.add_field(name="Número de riquezas", value=rolls, inline=False)

    totalSum = 0
    for _, item in enumerate(treasures):
        bonus = item["bonus"]
        totalSum += sum(item["rolls"]) + bonus

    
    embed.add_field(name="Total das jogadas + bônus", value=f"{totalSum}", inline=False)

    return embed
