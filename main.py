from aula01.desafio1 import run as run_desafio_1
from aula01.desafio2 import run as run_desafio_2
from aula01.desafio3 import run as run_desafio_3
from aula01.desafio4 import run as run_desafio_4
from aula01.desafio5 import run as run_desafio_5
from aula01.desafio6 import run as run_desafio_6
from aula01.desafio7 import run as run_desafio_7

desafios = {
    '1': run_desafio_1,
    '2': run_desafio_2,
    '3': run_desafio_3,
    '4': run_desafio_4,
    '5': run_desafio_5,
    '6': run_desafio_6,
    '7': run_desafio_7
}

if __name__ == "__main__":
    desafio = input(
        'Qual desafio gostaria de executar (1, 2, 3, 4, 5, 6 ou 7)?\n')

    if desafio in desafios:
        desafios[desafio]()
    else:
        print('O desafio não foi encontrado!')
