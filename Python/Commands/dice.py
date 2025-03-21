import random

# TODO Better formmating
# TODO Add tagged rolls and multiple rolls
async def roll_dice(ctx, dice_value: int, dice_qtd: int, dice_bonus: int):
    if dice_qtd > 50:
        await ctx.send(str(dice_qtd) + " dados ultrapassa o limite definido, por favor mantenha abaixo de 50 dados.")
    else:
        result = 0
        dices = []
        dice_index = 0
        while dice_index < dice_qtd:
            num = random.randrange(1, dice_value)
            dices.append(num)
            dice_index += 1
        index_addition = 0
        while index_addition < len(dices):
            result += dices[index_addition]
            index_addition += 1

        await ctx.send ("**" + str(result + dice_bonus) + "** <- " + str(dices) + " " + str(dice_bonus))