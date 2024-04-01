def ordenacao_selecao(lst: list):
    for i in range(len(lst)):
        m = i # índice do menor em lst[i:]
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]


def ordenacao_insercao(lst: list[int]):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j - 1] > lst[j]:
            lst[j - 1], lst[j] = lst[j], lst[j - 1]
            j -= 1

def merge_sort(lista: list[int]):
    if len(lista) > 1:
        meio = len(lista) // 2
        metade_esquerda = lista[:meio]
        metade_direita = lista[meio:]

        merge_sort(metade_esquerda)
        merge_sort(metade_direita)

        i = j = k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            if metade_esquerda[i] < metade_direita[j]:
                lista[k] = metade_esquerda[i]
                i += 1
            else:
                lista[k] = metade_direita[j]
                j += 1
            k += 1

        while i < len(metade_esquerda):
            lista[k] = metade_esquerda[i]
            i += 1
            k += 1

        while j < len(metade_direita):
            lista[k] = metade_direita[j]
            j += 1
            k += 1

    return lista

def heapify(arr: list[int], n: int, i: int):
    maior = i  
    esquerda = 2 * i + 1  
    direita = 2 * i + 2  

    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda

    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]  

        heapify(arr, n, maior)

def heap_sort(arr: list[int]):
    n = len(arr)

    # Construir um max heap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrair elementos um por um do heap.
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Trocar
        heapify(arr, i, 0)

    return arr

def isOrdem(lst: list[int]) -> bool:
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            return False
        
    return True 