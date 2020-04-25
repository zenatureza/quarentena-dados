"""
Desafio 3 do Guilherme Silveira
Colocar o número de avaliações por filme, isto é, não só a média mas o TOTAL de votos por filme.
"""

from api.get_data import *


def run():
    filmes = get_filmes()
    avaliacoes = get_avaliacoes()

    notas_medias_por_filme = avaliacoes.groupby("filmeId")["nota"].mean()
    numero_notas_por_filme = avaliacoes.groupby("filmeId")["nota"].count()

    filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
    filmes = filmes_com_media.merge(
        numero_notas_por_filme, on="filmeId", how="left")

    filmes.rename(columns={'nota_x': 'notaMédia',
                           'nota_y': 'quantidadeVotos'}, inplace=True)

    print('Filmes com nota média e quantidade de votos por filme:')
    print(filmes)
