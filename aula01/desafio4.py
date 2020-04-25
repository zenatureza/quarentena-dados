"""
Desafio 4 do Thiago Gonçalves

Arredondar as médias (coluna de nota média) para duas casas decimais.
"""

from api.get_data import get_filmes_com_nota_media


def run():
    filmes_com_nota_media = get_filmes_com_nota_media()

    filmes_com_nota_media['notaMédia'] = filmes_com_nota_media['notaMédia'].round(
        2)
    print(filmes_com_nota_media)
