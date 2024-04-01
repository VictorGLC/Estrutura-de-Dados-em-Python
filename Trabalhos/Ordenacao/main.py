import timeit
import random
from ordenacoes import *

def gera_numero(inicio: int, fim: int) -> int:
    return random.randint(inicio, fim)

def randomiza(inicio: int, fim: int, tam: int) -> list[int]:
    lst: list[int] = []
    while len(lst) < tam:
        lst.append(gera_numero(inicio,fim))
    return lst

lst_cem = randomiza(0, 100000000, 100)
lst_mil = randomiza(0, 100000000, 1000)
lst_dezmil = randomiza(0, 100000000, 10000)
lst_milhao = randomiza(0, 100000000, 1000000)

tempo_execucao_cem = timeit.timeit(lambda: ordenacao_selecao(lst_cem), number=1)
tempo_execucao_mil = timeit.timeit(lambda: ordenacao_selecao(lst_mil), number=1)
tempo_execucao_dezmil = timeit.timeit(lambda: ordenacao_selecao(lst_dezmil), number=1)
tempo_execucao_milhao = timeit.timeit(lambda: ordenacao_selecao(lst_milhao), number=1)

print('Tempo lista cem:',round(tempo_execucao_cem, 5), 's')
print('Tempo lista mil:',round(tempo_execucao_mil, 5), 's')
print('Tempo lista dez mil:',round(tempo_execucao_dezmil, 5), 's')
print('Tempo lista milhão:',round(tempo_execucao_milhao, 5), 's')

