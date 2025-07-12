from enum import Enum

class Type_treasure(Enum):
    DINHEIRO = (0, "Dinheiro")
    RIQUEZA_MENOR = (1, "Riqueza menor")
    RIQUEZA_MENOR_BONUS = (2, "Riqueza Menor com Bônus")
    RIQUEZA_MEDIA = (3, "Riqueza Média")
    RIQUEZA_MEDIA_BONUS = (4, "Riqueza Média com Bônus")
    RIQUEZA_MAIOR = (5, "Riqueza Maior")
    RIQUEZA_MAIOR_BONUS = (6, "Riqueza Maior com Bônus")

print(Type_treasure.DINHEIRO.value)    
