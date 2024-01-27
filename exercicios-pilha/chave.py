from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    chave: int
    valor: int | None

class Pilha:
    def __init__(self, tam_max: int):
        self.elementos: list[Item] = [Item(None, None)] * tam_max
        self.tam_max = tam_max
        self.topo = 0

    def vazia(self) -> bool:
        return self.topo == 0

    def cheia(self) -> bool:
        return self.topo == self.tam_max

    def empilha(self, chave: int, valor: int | None):
        if self.cheia():
            raise ValueError('Pilha Cheia')
        else:
            self.elementos[self.topo] = Item(chave, valor)
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
            return deepcopy(self.elementos[self.topo - 1])

    def remove_item_por_chave(self, chave: int) -> Item:
        pilha_aux = Pilha(self.tam_max)

        item_removido = None

        while not self.vazia():
            elemento = self.desempilha()
            if elemento.chave == chave:
                item_removido = elemento
            else:
                pilha_aux.empilha(elemento.chave, elemento.valor)

        while not pilha_aux.vazia():
            elemento = pilha_aux.desempilha()
            self.empilha(elemento.chave, elemento.valor)

        return item_removido

# Exemplo de uso
p = Pilha(5)

p.empilha(1, 10)
p.empilha(2, 20)
p.empilha(3, 30)
p.empilha(4, 40)
p.empilha(5, 50)

remove_chave = 4
item_removido = p.remove_item_por_chave(remove_chave)

if item_removido:
    print(f"Item removido com chave {remove_chave}: Valor {item_removido.valor}")
else:
    print(f"Nenhum item removido com chave {remove_chave}")

print("Pilha após a remoção:")
while not p.vazia():
    elemento = p.desempilha()
    print(f"Chave: {elemento.chave}, Valor: {elemento.valor}")