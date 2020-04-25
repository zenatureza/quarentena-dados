import pandas as pd


def get_avaliacoes():
    avaliacoes = pd.read_csv(
        "https://github.com/alura-cursos/introducao-a-data-science/blob/master/aula0/ml-latest-small/ratings.csv?raw=true")

    avaliacoes.columns = ['usuarioId', 'filmeId', 'nota', 'timestamp']

    return avaliacoes


def get_filmes():
    filmes = pd.read_csv(
        "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula0/ml-latest-small/movies.csv")

    filmes.columns = ["filmeId", "titulo", "generos"]

    return filmes


def get_filmes_com_nota_media():
    filmes = get_filmes()
    avaliacoes = get_avaliacoes()

    notas_medias_por_filme = avaliacoes.groupby("filmeId")["nota"].mean()

    filmes_com_media = filmes.join(notas_medias_por_filme, on="filmeId")
    filmes_com_media.rename(columns={'nota': 'notaMédia'}, inplace=True)

    return filmes_com_media


def get_array_lista_generos():
    filmes = get_filmes()
    array_lista_generos = filmes['generos'].apply(
        lambda genero: genero.split('|')).to_numpy()

    return array_lista_generos


def get_generos_unicos():
    array_lista_generos = get_array_lista_generos()
    generos_unicos = {e for l in array_lista_generos for e in l}

    return generos_unicos


def get_numero_aparicoes_generos():
    array_lista_generos = get_array_lista_generos()

    numero_aparicoes_generos = {}
    for lista_generos in array_lista_generos:
        for genero in lista_generos:
            if genero not in numero_aparicoes_generos:
                numero_aparicoes_generos[genero] = 0

            numero_aparicoes_generos[genero] += 1

    return numero_aparicoes_generos
