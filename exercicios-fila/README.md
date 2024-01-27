# Lista de Exercícios sobre Filas e Pilhas

## Código Inicial - Fila

```python
from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy, copy

@dataclass
class Item:
    valor: int | None

class Fila:
    def __init__(self, tam_max: int):
        self.elementos: list[Item] = [Item(None)] * tam_max
        self.tam_max = tam_max
        self.fim = 0
        
    def vazia(self) -> bool:
        return self.fim == 0
    
    def cheia(self) -> bool:
        return self.fim == self.tam_max
    
    def enfileira(self, x: Item):
        if self.cheia():
            raise ValueError('Fila cheia')
        else:
            self.elementos[self.fim] = deepcopy(x)
            self.fim += 1
    
    def desenfileira(self):
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            for i in range(1,self.fim):
                self.elementos[i-1] = self.elementos[i]
            self.fim -= 1
    
    def obtem_primeiro(self) -> Item:
        if self.vazia():
            raise ValueError('Fila vazia')
        else:
            return deepcopy(self.elementos[0])
```
## Código Inicial - Pilha 

```python
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
            self.topo += 1
```

## Exercício 1

Reescreva a função "Desenfileira" para que ela, além de remover o primeiro elemento da fila, retorne este elemento para ser mostrado na tela.

## Exercício 2

Considere uma fila com vários elementos numéricos. Liste apenas os elementos pares desta fila.

## Exercício 3

Considere a estrutura de uma fila e uma pilha. Faça uma função que receba um valor. Se o valor for positivo, insira na pilha. Caso contrário, insira na fila.

## Exercício 4

Escreva uma função em Python que inverta os elementos de uma fila, usando uma pilha como estrutura auxiliar.

--- 