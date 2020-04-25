"""
Desafio 5 do Allan Spadini
Descobrir os generos dos filmes (quais são eles, únicos). (esse aqui o bicho pega)
"""

from api.get_data import get_generos_unicos

import numpy as np


def run():
    generos_unicos = get_generos_unicos()

    print('Os genêros dos filmes são:')
    print(generos_unicos)
