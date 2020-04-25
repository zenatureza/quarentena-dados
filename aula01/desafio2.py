"""
Desafio 2 do Guilherme Silveira

Mudar o nome da coluna nota do dataframe filmes_com_media para nota_média após o join.
"""

from api.get_data import get_filmes_com_nota_media


def run():
    filmes_com_nota_media = get_filmes_com_nota_media()

    print(filmes_com_nota_media)
