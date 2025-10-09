import random

from core.equipament.armor.service import get_armor
from core.equipament.weapon.service import get_weapon
from core.equipament.esoteric.service import get_esoteric

async def get_type():

    d6 = random.randint(1, 6)

    return await get_weapon() if d6 <= 3 else await get_armor() if d6 <= 5 else await get_esoteric()