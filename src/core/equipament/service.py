import random

from core.equipament.armor.service import generate_armor
from core.equipament.weapon.service import generate_weapon
from core.equipament.esoteric.service import generate_esoteric

async def get_type():

    d6 = random.randint(1, 6)

    return await generate_weapon() if d6 <= 3 else await generate_armor() if d6 <= 5 else await generate_esoteric()