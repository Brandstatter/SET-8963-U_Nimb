import discord

from core.reward.treasure_enum import TreasureEnum

def embed_wealth(choseReward, treasures, rolls):
    wealthType = choseReward["description"]["wealth"]["type"]

    embed = discord.Embed(
        title="Prêmio",
        description="Wip",
        color=discord.Color.random() 
    )

    embed.add_field(name="Tipo de Riqueza", value=TreasureEnum.from_code(wealthType), inline=False)
    embed.add_field(name="Número de riquezas", value=rolls, inline=False)

    totalSum = 0
    for index, item in enumerate(treasures):
        bonus = item["bonus"]
        totalSum += sum(item["rolls"]) + bonus

        rollsStr = " + ".join(str(r) for r in item["rolls"])
        equation = f"jogadas: {rollsStr} + bonus: {bonus}"

        embed.add_field(name="\u200b", value="\u200b", inline=False)

        embed.add_field(
            name=f"Jogada: {str(index + 1)}",
            value=equation,
            inline=False
        )
        embed.add_field(name="Total das jogadas + bonus", value=f"{totalSum}", inline=False)

    return embed
