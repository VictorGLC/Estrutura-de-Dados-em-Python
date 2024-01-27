from __future__ import anNotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    valor: int

class No:
    def __init__(self, x: Item):
        self.dado: Item = x
        self.prox: No | None = None

class Pilha:
    def __init__(self):
        self.topo: No | None = None
  
    def vazia(self) -> bool:
        return self.topo == None

    def empilha(self, x: Item):
        Novo = No(x)
        Novo.prox = self.topo
        self.topo = Novo

    def desempilha(self):
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            rem = self.topo
            self.topo = self.topo.prox
            rem.prox = None

    def elemento_topo(self) -> Item:
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            dado = self.topo.dado
            ret:Item = deepcopy(dado.valor)
            return ret

    def imprime_pilha(self): #usar apenas para teste
        p = self.topo
        while p != None:
            print("Elemento: ", p.dado.valor)
            p = p.prox
        print("-------------------------")