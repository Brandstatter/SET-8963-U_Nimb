import discord

from core.reward.treasure_enum import TreasureEnum

def embed_wealth(choseReward, treasures, rolls, d100Main, d100Wealth):
    embeds = []
    wealthType = choseReward["description"]["wealth"]["type"]

    embed = discord.Embed(
        title=TreasureEnum.from_code(wealthType),
        description=None,
        color=discord.Color.random(),
        image="https://media.istockphoto.com/id/1705567435/pt/foto/treasury-hall-treasure-trove-of-gold-coins-and-chests-and-treasure-boxes-pile-up-treasuries.jpg?s=612x612&w=0&k=20&c=tJutkYQP40vE8ymqi66stHLXfRK3d4Pm56wpFjEMsQw="
    )
    embed.add_field(name="D100 Recompensa", value=d100Main, inline=False)
    embed.add_field(name="Número de riquezas", value=rolls, inline=False)

    if(choseReward["description"]["wealth"].get("incentive")):
        embed.add_field(name="+ 20%", value="Sim", inline=False)
    else:
        embed.add_field(name="+ 20%", value="Não", inline=False)

    totalSum = 0
    for index, item in enumerate(treasures):
        bonus = item["bonus"]
        totalSum += sum(item["rolls"]) * bonus

        embeds.append(rollsEmbed(index=index, treasure=item))

    embed.add_field(name="Recompensa total", value=f"T$ {totalSum}", inline=False)
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
    equation = f"{numberOfRolls}d{dice} -> `{rollsStr}` = {totalSum} * {bonus} = T$ {totalSum * bonus}" 

    embed = discord.Embed(
        title=f"Jogada: {index + 1}",
        description=f"{equation}",
        color=discord.Color.random()
    )

    embed.add_field(name="Multiplicador de valor", value=bonus, inline=False)
    embed.add_field(name="Exemplos de prêmios", value=examplesString, inline=False)

    return embed

