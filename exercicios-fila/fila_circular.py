from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy, copy


@dataclass
class item:
    valor: int

class fila:
    def __init__(self, tam_max: int):
        self.tamanho = tam_max
        self.inicio = 0
        self.fim = 0
        self.elementos: list[item] = [item(None) for i in range(tam_max)]
    
    def proximo_indice(self, i: int) -> int:
        return (i+1) % self.tamanho
    
    def vazia(self) -> bool:
        return self.inicio == self.fim
    
    def cheia(self) -> bool:
        return self.proximo_indice(self.fim) == self.inicio
    
    def enfileira(self, x: item):
        if self.cheia():
            raise ValueError('Fila cheia')
        else:
            self.elementos[self.fim] = deepcopy(x)
            self.fim = self.proximo_indice(self.fim)
    
    def desenfileira(self): 
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            self.inicio = self.proximo_indice(self.inicio)
    
    def obtem_primeiro(self) -> item:
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.elementos[self.inicio])