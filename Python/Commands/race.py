import discord
import json

RACES_JSON = json.load(open("json\detail_races.json", encoding='utf-8'))

async def switcher_race(name):
    match name:
        case "Humano":
            return 0   
        case "Anão":
            return 1
        case "Dahllan":
            return 2
        case "Elfo":
            return 3
        case "Goblin":
            return 4
        case "Lefou":
            return 5
        case "Minotauro":
            return 6
        case "Qareen":
            return 7 
        case "Golem":
            return 8
        case "Hynne":
            return 9
        case "Kliren":
            return 10
        case "Medusa":
            return 11
        case "Osteon":
            return 12
        case "Sereia/Tritão":
            return 13
        case "Sílfide":
            return 14
        case "Suraggel":
            return 15
        case "Trog":
            return 16

async def search_race(ctx):
    race_select = discord.ui.Select(options=[
        discord.SelectOption(label="Humano"),
        discord.SelectOption(label="Anão"),
        discord.SelectOption(label="Dahllan"),
        discord.SelectOption(label="Elfo"),
        discord.SelectOption(label="Goblin"),
        discord.SelectOption(label="Lefou"),
        discord.SelectOption(label="Minotauro"),
        discord.SelectOption(label="Qareen"),
        discord.SelectOption(label="Golem"),
        discord.SelectOption(label="Hynne"),
        discord.SelectOption(label="Kliren"),
        discord.SelectOption(label="Medusa"),
        discord.SelectOption(label="Osteon"),
        discord.SelectOption(label="Sereia/Tritão"),
        discord.SelectOption(label="Sílfide"),
        discord.SelectOption(label="Suraggel"),
        discord.SelectOption(label="Trog"),
    ])

    async def race_callback(interaction):
        choosen = str({race_select.values[0]})
        id = await switcher_race(choosen[2:-2])
        embed = await embed_race(ctx, id)
        await interaction.response.send_message(embed=embed)

    race_select.callback = race_callback
    view = discord.ui.View(race_select)
    await ctx.send(view = view)

async def embed_race(ctx, id):
    name = str(RACES_JSON[id]['name']).encode('latin-1')
    atribute = str(RACES_JSON[id]['atributes']).encode('latin-1')

    race = discord.Embed(
    title = name.decode('latin-1'),
    description = "**Atributos** \n" + atribute.decode('latin-1'),
    color = discord.Color.random())

    x = 0
    while x < len(RACES_JSON[id]['skills']['titles']):
        race.add_field(name=str(RACES_JSON[id]['skills']['titles'][x]), value=str(RACES_JSON[id]['skills']['description'][x]), inline=False)
        x = x+1

    return race
    