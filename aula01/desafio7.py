"""
Desafio 7 do Guilherme Silveira
Plotar o gráfico de aparições de cada genero. Pode ser um gráfico de tipo igual a barra.
"""

from api.get_data import get_numero_aparicoes_generos
import pandas as pd
import matplotlib.pyplot as plt


def run():
    numero_aparicoes_generos = get_numero_aparicoes_generos()

    generos = list(numero_aparicoes_generos.keys())
    aparicoes = list(numero_aparicoes_generos.values())

    numero_aparicoes_generos_df = pd.DataFrame(
        {'Número de aparições': aparicoes}, index=generos)

    print(numero_aparicoes_generos_df)

    numero_aparicoes_generos_df.plot.bar(rot=0)
    plt.title('Número de aparições de gêneros de filmes')
    plt.show()
