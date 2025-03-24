import discord
from discord.ui import View


async def set_attributes(dices : list):
    # TODO switcher a function on itself
    attribute_choice = discord.Embed(title = "Definir atributos", color = 2899536)
    attribute_choice.add_field(title="Escolha o valor do atributo força.")
    attributes_select = View()
    button1 = discord.ui.Button(emoji=":4948_rainbow_crit_fail:", style = discord.ButtonStyle.green, custom_id = '1')
 
def button_swicther(dices:list):
    for dice in dices:
        match dice:
            case 1:
                return 1
            case 2:
                return 2
            case 3:
                return 3
            case 4:
                return 4
            case 5:
                print(5)
            case 6:
                print(6)
            case 7:
                print(7)
            case 8:
                print(8)
            case 9:
                print(9)
            case 10:
                print(10)
            case 11:
                print(11)
            case 12:
                print(12)
            case 13:
                print(13)
            case 14:
                print(14)
            case 15:
                print(15)
            case 16:
                print(16)
            case 17:
                print(17)
            case 18:
                print(18)