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

    def imprimeLista(self):
      for i in range(self.tam):
        if self.elementos[i] != None:
          print(f"Chave: {self.elementos[i].chave}, Valor: {self.elementos[i].valor}")

    def remove_chave(self, ch: int) -> bool:
      indice = self.busca(ch)
      if indice != -1:
          self.__desloca(indice)
          self.tam -= 1
          return True
      return False

    def insere_ord(self, x: Item) -> bool:
      if not self.cheia():
          i = 0
          while i < self.tam and self.elementos[i].chave < x.chave:
              i += 1

          for j in range(self.tam, i, -1):
              self.elementos[j] = self.elementos[j-1]

          self.elementos[i] = deepcopy(x)
          self.tam += 1
          return True

      return False

#Exercicio 1
print("Exercio 1")
l = Lista(5)

l.insere_fim(Item(1, 5))
l.insere_fim(Item(2, 10))
l.insere_fim(Item(3, 15))
l.insere_fim(Item(4, 20))

l.imprimeLista()

print("----------------------------------------")
# Exercicio 2
print("Exercicio 2")
l = Lista(5)

l.insere_fim(Item(1, 10.5))
l.insere_fim(Item(2, 20.0))
l.insere_fim(Item(3, 30.8))

print("Lista antes da remoção:")
l.imprimeLista()

chave_removida = 2
l.remove_chave(chave_removida)

print("\nLista após a remoção da chave", chave_removida, ":")
l.imprimeLista()

print("----------------------------------------")
# Exercicio 3
print("Exercicio 3")
l = Lista(5)

l.insere_ord(Item(5, 30.8))
l.insere_ord(Item(1, 10.5))
l.insere_ord(Item(3, 20.0))

print("Lista ordenada:")
l.imprimeLista()


