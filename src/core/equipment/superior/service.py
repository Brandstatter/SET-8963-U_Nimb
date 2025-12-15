import os
import json
import random

json_path = os.path.join("json", "equipament/superior/improvements.json")
IMPROVEMENT_JSON = json.load(open(json_path, encoding='utf-8'))

json_path = os.path.join("json", "equipament/superior/improvements_table.json")
TABLE_JSON = json.load(open(json_path, encoding='utf-8'))

async def special_material(embed, material_type):
    material = IMPROVEMENT_JSON[19]['material'][random.randint(0,5)]

    name = material['name_material']
    effect = material['effects'][material_type]['item_effect']
    desc = material['desc_material']

    embed.add_field(
        name=f"Material Especial - {name}",
        value=f"Efeito: {effect}\n{desc}",
        inline = False
    )

    return embed

async def add_improvement(embed, improvement_id, item_type):

    if isinstance(improvement_id, list):

        if embed.description == "**Escudos**":
            improvement = IMPROVEMENT_JSON[13]
        else:
            improvement = IMPROVEMENT_JSON[12]
    else:
        improvement = IMPROVEMENT_JSON[improvement_id]

    if improvement_id == 19:
        return await special_material(embed, item_type)

    embed.add_field(
        name=improvement['name'],
        value=f"Efeito: {improvement['effect']}\n{improvement['desc']}",
        inline = False
    )

    return embed

async def get_superior(embed, item_type, qtd):
    selected_reward = set()

    while len(selected_reward) < qtd:
        d100 = random.randint(1, 100)

        for item in TABLE_JSON[item_type]['table']:
            if d100 <= item['cutoffValue']:
                print(item['rewardId'])
                print(IMPROVEMENT_JSON[item['rewardId']]['required'])
                if IMPROVEMENT_JSON[item['rewardId']]['required'] is not None:
                    selected_reward.add(IMPROVEMENT_JSON[item['rewardId']]['required'])

                selected_reward.add(item['rewardId'])
                break
    
    for item in selected_reward:
        embed = await add_improvement(embed, item, item_type)


    return embed