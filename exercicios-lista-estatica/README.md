```markdown
# Lista de Exercícios sobre Listas

Este repositório contém uma lista de exercícios relacionados a um TAD (Tipo Abstrato de Dados) de Listas. O código inicial para os exercícios está abaixo.

## Código Inicial

```python
from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    chave: int
    valor: float

class Lista:
    def __init__(self, tamanho: int):
        self.tam: int = 0
        self.tam_max: int = tamanho
        self.elementos: list[Item | None] = [None] * tamanho
    
    def vazia(self) -> bool:
        return self.tam == 0
    
    def cheia(self) -> bool:
        return self.tam == self.tam_max

    def busca(self, ch: int) -> int:
        for i in range(self.tam):
            if self.elementos[i].chave == ch:
                return i
        return -1

    def busca_item(self, ch: int) -> Item | None:
        idx = self.busca(ch)
        if idx != -1:
            return deepcopy(self.elementos[idx])
        else:
            return None

    def insere_fim(self, x: Item) -> bool:
        if (not self.cheia()) and (self.busca(x.chave) == -1):
            self.elementos[self.tam] = deepcopy(x)
            self.tam += 1
            return True
        return False

    def insere_pos(self, x: Item, pos: int) -> bool:
        if (not self.cheia()) and (pos <= self.tam) and (self.busca(x.chave) == -1):
            for i in range(self.tam, pos, -1):
                self.elementos[i] = self.elementos[i-1]
            self.elementos[pos] = deepcopy(x)
            self.tam += 1
            return True
        return False

    def __desloca(self, pos: int):
        for i in range(pos+1, self.tam):
            self.elementos[i-1] = self.elementos[i]

    def remove_fim(self) -> bool:
        if not self.vazia():
            self.tam -= 1
            return True
        return False

    def remove_pos(self, pos: int) -> bool:
        if not self.vazia():
            self.__desloca(pos)
            return True
        return False
```

## Exercícios

### Exercício 1

Adicione ao TAD Listas uma função `ImprimeLista` para exibir todos os itens armazenados na lista.

### Exercício 2

Adicione ao TAD Listas uma função para remover um item a partir do valor da chave.

### Exercício 3

Supondo que o campo chave dos itens esteja em ordem crescente, adicione ao TAD uma função `InsereORD` para que ela mantenha os itens ordenados após a inserção do item desejado.

