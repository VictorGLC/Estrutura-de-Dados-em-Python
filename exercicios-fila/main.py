from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class item:
    valor: int | None

class pilha:
    def __init__(self, tam_max: int):
        self.elementos: list[item] = [item(None)] * tam_max
        self.tam_max = tam_max
        self.topo = 0

    def vazia(self) -> bool:
        return self.topo == 0

    def cheia(self) -> bool:
        return self.topo == self.tam_max

    def empilha(self, x: item):
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

        return deepcopy(self.elementos[self.topo])

    def consulta_topo(self) -> item:
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            return deepcopy(self.elementos[self.topo-1])

class fila:
    def __init__(self, tam_max: int):
        self.elementos: list[item] = [item(None)] * tam_max
        self.tam_max = tam_max
        self.fim = 0
    
    def vazia(self) -> bool:
        return self.fim == 0
    
    def cheia(self) -> bool:
        return self.fim == self.tam_max
    
    def enfileira(self, x: item):
        if self.cheia():
            raise ValueError('Fila cheia')
        else:
            self.elementos[self.fim] = deepcopy(x)
            self.fim += 1
    
    def desenfileira(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            primeiro_elemento = deepcopy(self.elementos[0])

            for i in range(1,self.fim):
                self.elementos[i-1] = self.elementos[i]
            self.fim -= 1

            return primeiro_elemento
    
    def obtem_primeiro(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.elementos[0])

    def inverte_elementos(self):
        if self.vazia():
            raise ValueError('Fila vazia')

        pilha_auxiliar = pilha(self.tam_max)

        # Empilhar elementos da fila na pilha auxiliar
        while not self.vazia():
            pilha_auxiliar.empilha(self.desenfileira())

        # Desempilhar elementos da pilha e enfileirar de volta na fila
        while not pilha_auxiliar.vazia():
            self.enfileira(pilha_auxiliar.desempilha())
    
    def listaPares(self) -> list[int]:
        pares: list[int] = []

        for i in range(self.tam_max):
          item = self.elementos[i].valor
          if item is not None and item % 2 == 0:
            pares.append(item)
              
        return pares

def insereValor(f: fila, p: pilha, valor: int):
    if valor > 0 and not p.cheia():
        p.empilha(item(valor))
    elif valor < 0 and not f.cheia():
        f.enfileira(item(valor))

p = pilha(5)
p.empilha(item(1))
p.empilha(item(4))

f = fila(5)

f.enfileira(item(5))
f.enfileira(item(6))
f.enfileira(item(7))
f.enfileira(item(8))

print(f.listaPares())
print(f.obtem_primeiro())
f.inverte_elementos()
print(f.listaPares())
print(f.obtem_primeiro())
print(f.desenfileira())