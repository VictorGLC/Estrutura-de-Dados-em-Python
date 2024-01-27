# Lista de Exercícios sobre Pilhas

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
            
    def desempilha(self):
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            self.topo = self.topo - 1

    def consulta_topo(self) -> Item:
        if self.vazia():
            raise ValueError('Pilha Vazia')
        else:
            return deepcopy(self.elementos[self.topo-1])
```

## Exercício 1

Considere o seguinte conjunto de números 1234 e as seguintes operações:

- (a) Inserir o 1 na pilha;
- (b) Inserir o 2 na pilha;
- (c) Retirar o 2 da pilha;
- (d) Inserir o 3 na pilha;
- (e) Inserir o 4 na pilha;
- (f) Retirar o 4 da pilha;
- (g) Retirar o 3 da pilha;
- (h) Retirar o 1 da pilha.

A sequência de saídas do procedimento acima é 2431. Considere agora a sequência 123456. Podemos obter as sequências 325641 e 154623 utilizando um processo semelhante ao do exemplo anterior? Descreva o processo.

## Exercício 2

Reescreva a função "Desempilha" para que ela desempilhe o topo da pilha e retorne o item desempilhado.

## Exercício 3

Escreva uma função em Python que imprima os elementos de uma pilha na mesma ordem em que eles foram empilhados (pode ser usada uma pilha auxiliar).

## Exercício 4

Utilizando somente operações de empilhar e desempilhar, escreva uma função que remove um item com chave c fornecida pelo usuário da pilha. Ao final da execução da função, a pilha deve ser igual à original, exceto pela ausência do item removido.

## Exercício 5

Considere uma pilha com vários elementos numéricos. Liste apenas os elementos pares desta pilha.

---
