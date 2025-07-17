import os
import discord
import json
import random
import math

json_path = os.path.join("json", "chaos_cards.json")
CARDS_JSON = json.load(open(json_path, encoding='utf-8'))

async def draw_cards(card_qtd):
    cards = []
    
    for card in range(card_qtd):
        d100 = random.randrange(1, 100)
        percentages = CARDS_JSON['percentages']
        index = 0

        while d100 > percentages[index]:
            index += 1
        index = int(math.floor(index/2))

        cards.append(CARDS_JSON['cards'][index]['id'])

    embed = await embed_card(cards)
    return embed

async def embed_card(id_list):
    name = "Cartas sacadas"
    description = ""

    for id in id_list:
        card = f'## {CARDS_JSON["cards"][id]["name"]}\n {CARDS_JSON["cards"][id]["effect"]} \n {CARDS_JSON["cards"][id]["desc"]} \n\n'
        description = description + card

    embed = discord.Embed(
    title = name,
    description = description,
    color=discord.Color.random())

    return embed
