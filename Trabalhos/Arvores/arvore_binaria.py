from dataclasses import dataclass

@dataclass
class Item:
  chave: int

class No:
  def __init__(self, dado: Item):
    self.esq: No | None = None
    self.dir: No | None = None
    self.dado: Item = dado
    self.altura: int = 1

class Arvore:
  def __init__(self):
    self.raiz: No | None = None

  def vazia(self):
    return self.raiz == None
  
  def busca(self, ch:int) -> Item | None:
    no = self.busca_No(self.raiz, ch)
    if no != None:
      return no.dado
    else:
      return None

  def busca_No(self, n: No, chave:int) -> No | None:
    if n == None:
      return None
    elif chave > n.dado.chave:
      return self.busca_No(n.dir, chave)
    elif chave < n.dado.chave:
      return self.busca_No(n.esq, chave)
    else:
      return n

  def insere(self, x: Item):
    self.raiz = self.insere_no(self.raiz, x)

  def insere_no(self, n: No , x: Item) -> No | None:
    if n == None:
      n = No(x)
    elif x.chave > n.dado.chave:
      n.dir = self.insere_no(n.dir,x)
    elif x.chave < n.dado.chave:
      n.esq = self.insere_no(n.esq,x)
    if n != None:
      n.altura = self.altura(n)  
    return n
      
  def remove(self, chave: int):
    self.raiz = self.remove_no(self.raiz, chave)

  def remove_no(self, n: No, chave: int) -> No | None:
    if n != None:
      if n.dado.chave < chave:
        n.dir = self.remove_no(n.dir, chave)
      elif n.dado.chave > chave:
        n.esq = self.remove_no(n.esq, chave)
      else:
        if n.esq != None and n.dir != None:
          antecessor = self.maior(n.esq)
          n.dado = antecessor.dado
          self.remove_no(n.esq, antecessor.dado.chave)
        elif n.esq == None:
          n = n.dir
        else:
          n = n.esq
    return n

  def maior(self, n: No) -> No:
    if n.dir == None:
      return n
    else:
      return self.maior(n.dir)
    
  def altura(self, no: No) -> int:
    '''
    Retorna a altura de um nó na árvore.

    Exemplo:
    >>> arvore = Arvore()
    >>> arvore.insere(Item(2))
    >>> arvore.insere(Item(1))
    >>> arvore.insere(Item(3))
    >>> arvore.insere(Item(5))
    >>> arvore.insere(Item(4))
    >>> arvore.insere(Item(6))
    >>> arvore.altura(arvore.raiz)
    4
    
    >>> t = Arvore()
    >>> p = No(Item(2))
    >>> q = No(Item(8))
    >>> w = No(Item(3))

    >>> r = No(Item(3))
    >>> s = No(Item(7))
    >>> u = No(Item(5))

    >>> x = No(Item(4))
    >>> z = No(Item(2))
    
    >>> t.raiz = p
    >>> p.esq = q
    >>> p.dir = w

    >>> q.esq = r
    >>> w.esq = s
    >>> w.dir = u

    >>> r.esq = x
    >>> u.dir = z
    >>> t.altura(p)
    4
    '''
    if no is None:
      return 0
    altura_esq = self.altura(no.esq)
    altura_dir = self.altura(no.dir)
    return max(altura_esq, altura_dir) + 1