from arvore_binaria import *

def elemInOrdem(no: No) -> list[int]:
  '''
  A partir de um nó de uma árvore binária de busca retorna em uma lista 
  todos os seus elementos em ordem crescente (in ordem).
  
  Exemplo:
  >>> arvore1 = Arvore()
  >>> arvore1.insere(Item(1))
  >>> arvore1.insere(Item(5))
  >>> arvore1.insere(Item(6))
  >>> arvore1.insere(Item(8))
  >>> arvore1.insere(Item(10))
  >>> elemInOrdem(arvore1.raiz)
  [1, 5, 6, 8, 10]
  
  >>> arv3 = Arvore()
  >>> arv3.insere(Item(3))
  >>> arv3.insere(Item(5))
  >>> arv3.insere(Item(6))
  >>> arv3.insere(Item(2))
  >>> elemInOrdem(arv3.raiz)
  [2, 3, 5, 6]
  '''
  if no is None:
    return []
  return elemInOrdem(no.esq) + [no.dado.chave] + elemInOrdem(no.dir)

def mesmaArvore(arvore1: Arvore, arvore2: Arvore) -> bool:
  '''
  Verifica se duas árvores binárias de busca tem todos os mesmos elementos.

  Exemplo:
  >>> arvore1 = Arvore()
  >>> arvore1.insere(Item(1))
  >>> arvore1.insere(Item(5))
  >>> arvore1.insere(Item(6))
  >>> arvore1.insere(Item(8))
  >>> arvore1.insere(Item(10))
  
  >>> arvore2 = Arvore()
  >>> arvore2.insere(Item(1))
  >>> arvore2.insere(Item(10))
  >>> arvore2.insere(Item(6))
  >>> arvore2.insere(Item(8))
  >>> arvore2.insere(Item(5))
  >>> mesmaArvore(arvore1, arvore2)
  True
  
  >>> arv3 = Arvore()
  >>> arv3.insere(Item(3))
  >>> arv3.insere(Item(5))
  >>> arv3.insere(Item(6))
  >>> arv3.insere(Item(2))
  
  >>> arv4 = Arvore()
  >>> arv4.insere(Item(0))
  >>> arv4.insere(Item(2))
  >>> arv4.insere(Item(3))
  >>> arv4.insere(Item(4))
  >>> arv4.insere(Item(1))
  >>> mesmaArvore(arv3, arv4)
  False
  >>> mesmaArvore(arv3, arvore1)
  False
  >>> mesmaArvore(arv4, arvore2)
  False
  '''
  
  # Adiciona os elementos de ambas as árvores em uma lista
  lista1 = elemInOrdem(arvore1.raiz)
  lista2 = elemInOrdem(arvore2.raiz)

  # Compara as listas resultantes
  return lista1 == lista2