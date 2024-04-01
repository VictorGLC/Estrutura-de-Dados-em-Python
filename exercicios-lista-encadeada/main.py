from __future__ import annotations
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Item:
    chave: int
    valor: str

class No:
    def __init__(self, x: Item):
        self.dado: Item = x
        self.prox: No | None = None

class Lista:
    def __init__(self):
        self.primeiro: No | None = None
        self.ultimo: No | None = None

    def vazia(self):
        return self.primeiro is None

    def busca(self, chave: int) -> No | None:
        ptr = self.primeiro
        while ptr is not None and ptr.dado.chave != chave:
            ptr = ptr.prox
        return ptr

    def busca_item(self, chave: int) -> Item | None:
        ptr = self.busca(chave)
        if ptr is not None:
            return deepcopy(ptr.dado)
        else:
            return None

    def insere_ini(self, x: Item) -> bool:
        if self.busca(x.chave) is None:
            novo = No(x)
            if self.vazia():
                self.ultimo = novo
            novo.prox = self.primeiro
            self.primeiro = novo
            return True
        return False

    def remove_ini(self) -> bool:
        if not self.vazia():
            rem = self.primeiro
            self.primeiro = self.primeiro.prox
            if self.vazia():
                self.ultimo = None
            rem.prox = None
            return True
        return False

    def remove_chave(self, chave: int) -> bool:
        ptr = self.primeiro
        if not self.vazia():
            if ptr.dado.chave == chave:
                return self.remove_ini()
            while ptr.prox is not None and ptr.prox.dado.chave != chave:
                ptr = ptr.prox
            if ptr.prox is not None:
                rem = ptr.prox
                ptr.prox = rem.prox
                if ptr.prox is None:
                    self.ultimo = ptr
                rem.prox = None
                return True
        return False
   
    def insere_pos(self, x: Item, pos: int) -> bool:
        i = 0
        ptr = self.primeiro
        if pos == 0:
            return self.insere_ini(x)
        elif self.busca(x.chave) is None:
            while ptr is not None and i < pos - 1:
                ptr = ptr.prox
                i += 1
            if ptr is not None:
                novo = No(x)
                novo.prox = ptr.prox
                if novo.prox is None:
                    self.ultimo = novo
                ptr.prox = novo
                return True
        return False

    def exibir_lista(self):
        ptr = self.primeiro
        while ptr is not None:
            print('Chave:', ptr.dado.chave, '/ Valor:', ptr.dado.valor, end=" -> ")
            ptr = ptr.prox
        print("None")

    def contar_celulas(self) -> int:
        count = 0
        ptr = self.primeiro
        while ptr is not None:
            count += 1
            ptr = ptr.prox
        return count

    def concatenar(self, outra_lista: Lista):
        if not outra_lista.vazia():
            if self.vazia():
                self.primeiro = outra_lista.primeiro
                self.ultimo = outra_lista.ultimo
            else:
                self.ultimo.prox = outra_lista.primeiro
                self.ultimo = outra_lista.ultimo
            outra_lista.primeiro = None
            outra_lista.ultimo = None
    
l = Lista()
l.insere_ini(Item(1, 'A'))
l.insere_ini(Item(2, 'B'))

l.exibir_lista()

m = Lista()
m.insere_ini(Item(4, 'C'))
m.insere_ini(Item(3, 'D'))

l.concatenar(m)
l.exibir_lista()

l.insere_pos(Item(5, 'E'), 4)
l.exibir_lista()