import discord

def embed_money(choseReward, rolled_dice, d100):
    number_of_rolls = choseReward["description"]["numberOfRolls"]
    die_type = choseReward["description"]["chosenDie"]
    bonus = choseReward["description"].get("multiplier")
    currencyType = choseReward["description"]["currencyType"]

    totalSum = sum(rolled_dice)    
    totalSumPlusBonus = totalSum * bonus 

    rolls_str = " + ".join(str(r) for r in rolled_dice)
    equation = f"d{die_type}x{number_of_rolls} -> {rolls_str} = {totalSum} * {bonus} = {totalSumPlusBonus}"

    embed = discord.Embed(
        title="Prêmio",
        description=f"{equation}",
        color=discord.Color.random(),
        image="https://media.istockphoto.com/id/165418688/pt/foto/moedas-de-ouro.webp?a=1&b=1&s=612x612&w=0&k=20&c=_GmLZGwYwTmTEJDpSps31BVLG_8cn6WXLVx358Zrh_M="
    )

    fields = [
        ("D100", d100),
        ("Dados lançados", f"`{rolls_str}`"),
        ("Bônus", choseReward["description"]["multiplier"]),
        ("Resultado do prêmio", f"{totalSumPlusBonus} {currencyType}")
    ]

    for name, value in fields:
        embed.add_field(name=name, value=value, inline=False)

    return embed