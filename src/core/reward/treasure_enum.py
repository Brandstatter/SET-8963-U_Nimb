from enum import Enum

class TreasureEnum(Enum):
    RIQUEZA_MENOR = (1, "Riqueza Menor")
    RIQUEZA_MEDIA = (2, "Riqueza Média")
    RIQUEZA_SUPERIOR = (3, "Riqueza Superior")

    def __init__(self, code, description):
        self.code = code
        self.description = description

    @classmethod
    def from_code(cls, code):
        for status in cls:
            if status.code == code:
                return status.description
        return "Descricao não encontrada"        

