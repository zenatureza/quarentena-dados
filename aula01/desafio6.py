"""
Desafio 6 da Thais André
Contar o número de aparições de cada genero.
"""

from api.get_data import get_numero_aparicoes_generos


def run():
    numero_aparicoes_generos = get_numero_aparicoes_generos()

    print('O número de aparições dos generos é:')
    print(numero_aparicoes_generos)
