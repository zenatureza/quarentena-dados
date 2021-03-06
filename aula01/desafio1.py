"""
Desafio 1 do Paulo Silveira

O Paulo fez uma análise rápida e disse que tem 18 filmes sem avaliações, será que ele acertou?

Determine quantos filmes não tem avaliações e quais são esses filmes. 
"""

import pandas as pd
import numpy as np
from api.get_data import get_avaliacoes, get_filmes


def run():
    filmes = get_filmes()

    avaliacoes = get_avaliacoes()

    def get_filmes_sem_avaliacao(filmes, avaliacoes):
        filmes_e_respectivas_avaliacoes = filmes.merge(
            avaliacoes, on="filmeId", how="left", indicator="true")

        filmes_sem_avaliacao = filmes_e_respectivas_avaliacoes.query(
            'true != "both"')

        return filmes_sem_avaliacao

    filmes_sem_avaliacao = get_filmes_sem_avaliacao(filmes, avaliacoes)

    print("* Quantidade de filmes sem avaliação: {}\n".format(len(filmes_sem_avaliacao)))

    # gabarito
    id_filmes_sem_avaliacao = np.array(
        filmes_sem_avaliacao['filmeId'].to_numpy()).tolist()

    def get_avaliacoes_by_id_filmes(avaliacoes, id_filmes):
        """Obtém as avaliações dos filmes desejados, através dos seus ids

        Arguments:
            avaliacoes {pandas.DataFrame} -- Conjunto de avaliações de filmes
            id_filmes {List} -- Array de ids dos filmes a serem filtrados

        Returns:
            DataFrame -- Conjunto de avaliações dos filmes filtrados
        """
        return avaliacoes.query('filmeId in @id_filmes')

    print("* Avaliações dos filmes que teoricamento não possuem avaliação:")
    print(get_avaliacoes_by_id_filmes(avaliacoes, id_filmes_sem_avaliacao))
