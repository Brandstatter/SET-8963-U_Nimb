import random

from core.equipment.armor.service import generate_armor
from core.equipment.weapon.service import generate_weapon
from core.equipment.esoteric.service import generate_esoteric

async def get_type():

    d6 = random.randint(1, 6)

    return await generate_weapon() if d6 <= 3 else await generate_armor() if d6 <= 5 else await generate_esoteric()