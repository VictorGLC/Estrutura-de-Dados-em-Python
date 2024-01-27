from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
  valor: int | None

class Pilha:
  def __init__(self, tam_max: int):
    self.elementos: list[Item] = [Item(None)] * tam_max
    self.tam_max = tam_max
    self.topo = 0

  def vazia(self) -> bool:
    return self.topo == 0
  
  def cheia(self) -> bool:
    return self.topo == self.tam_max

  def empilha(self, x: Item):
    if self.cheia():
      raise ValueError('Pilha Cheia')
    else:
      self.elementos[self.topo] = deepcopy(x)
      self.topo = self.topo + 1

  def desempilha(self):
    if self.vazia():
      raise ValueError('Pilha Vazia')
    else:
      self.topo = self.topo - 1
      return deepcopy(self.elementos[self.topo]) # Exercício 2

  def consulta_topo(self) -> item:
    if self.vazia():
      raise ValueError('Pilha Vazia')
    else:
      return deepcopy(self.elementos[self.topo-1])

print('--------------------')
print('Exercício 1')

# Exercício 1
p = Pilha(4)

p.empilha(1)
p.empilha(2)
print('desempilhado:', p.desempilha())
p.empilha(3)
p.empilha(4)
print('desempilhado:', p.desempilha())
print('desempilhado:', p.desempilha())
print('desempilhado:', p.desempilha())
# saida: 2431

print('--------------------')

m = Pilha(6)

m.empilha(1)
m.empilha(2)
m.empilha(3)
print('desempilhado:', m.desempilha())
print('desempilhado:', m.desempilha())
m.empilha(4)
m.empilha(5)
print('desempilhado:', m.desempilha())
m.empilha(6)
print('desempilhado:', m.desempilha())
print('desempilhado:', m.desempilha())
print('desempilhado:', m.desempilha())
# saida: 325641

print('--------------------')

c = Pilha(6)

c.empilha(1)
print('desempilhado:', c.desempilha()) # 1
c.empilha(3)
c.empilha(2)
c.empilha(4)
c.empilha(5)
print('desempilhado:', c.desempilha()) # 5
print('desempilhado:', c.desempilha()) # 4
c.empilha(6)
print('desempilhado:', c.desempilha()) # 6
print('desempilhado:', c.desempilha()) # 2
print('desempilhado:', c.desempilha()) # 3
# saida: 154623

print('--------------------')
print('Exercício 3')
# Exercício 3
def imprime_pilha_na_ordem(pilha: Pilha):
    pilha_aux = Pilha(pilha.tam_max)

    # Transferir elementos para a pilha auxiliar para inverter a ordem
    while not pilha.vazia():
        elemento = pilha.desempilha()
        pilha_aux.empilha(elemento)

    # Imprimir os elementos na ordem original
    while not pilha_aux.vazia():
        elemento = pilha_aux.desempilha()
        print(elemento)

aux = Pilha(4)
aux.empilha(2)
aux.empilha(4)
aux.empilha(1)
aux.empilha(3)

imprime_pilha_na_ordem(aux)