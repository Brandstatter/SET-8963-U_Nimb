import os
import discord
import json
import random
import math

json_path = os.path.join("json", "chaos_cards.json")
CARDS_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "chaos_cards_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def draw_cards(card_qtd):
    cards = set()
    
    while len(cards) < card_qtd:
        d100 = random.randrange(1, 100)
        for item in TABLE_JSON:
            if d100 <= item['cutoffValue']:
                cards.add(item['rewardId'])
                break 
    
    embed = await embed_card(cards)
    return embed

async def embed_card(id_set):
    name = "Cartas sacadas"
    description = ""

    for id in id_set:
        card = f'## {CARDS_JSON[id]["name"]}\n {CARDS_JSON[id]["effect"]} \n {CARDS_JSON[id]["desc"]} \n\n'
        description = description + card

    embed = discord.Embed(
    title = name,
    description = description,
    color=discord.Color.random())

    return embed
    
    