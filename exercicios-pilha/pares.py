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

    def desempilha(self) -> Item:
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            self.topo = self.topo - 1
            return deepcopy(self.elementos[self.topo])

    def consulta_topo(self) -> Item:
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            return deepcopy(self.elementos[self.topo-1])

# Função para listar elementos pares da pilha
def listar_elementos_pares(pilha: Pilha):
    print("Elementos pares da pilha:")
    pilha_aux = Pilha(pilha.tam_max)

    while not pilha.vazia():
        elemento = pilha.desempilha()
        if elemento % 2 == 0:
            print(elemento)
        pilha_aux.empilha(elemento)

    while not pilha_aux.vazia():
        pilha.empilha(pilha_aux.desempilha())

# Exemplo de uso
p = Pilha(6)

p.empilha(1)
p.empilha(2)
p.empilha(3)
p.empilha(6)
p.empilha(5)
p.empilha(4)

listar_elementos_pares(p)
