from __future__ import annotations

class Figurinha:
  def __init__(self, figurinha: int):
    self.n_fig: int = figurinha
    self.quantidade: int = 1

class No:
  def __init__(self, x: Figurinha):
    self.dado: Figurinha = x
    self.prox: No | None = None

class Colecao:
  '''
  Uma coleção de figurinhas que é organizada em numeros por ordem crescente
  
  Exemplos:
  >>> c = Colecao(30)
  >>> c.possuidas()
  '[]'
  >>> c.repetidas()
  '[]'
  >>> c.insere(3)
  >>> c.insere(5)
  >>> c.insere(2)
  >>> c.possuidas()
  '[2, 3, 5]'
  >>> c.repetidas()
  '[]'
  >>> c.insere(5)
  >>> c.insere(15)
  >>> c.insere(3)
  >>> c.insere(5)
  >>> c.insere(2)
  >>> c.possuidas()
  '[2, 3, 5, 15]'
  >>> c.repetidas()
  '[2 (2), 3 (2), 5 (3)]'
  >>> c.remove(5)
  >>> c.remove(3)
  >>> c.possuidas()
  '[2, 3, 5, 15]'
  >>> c.repetidas()
  '[2 (2), 5 (2)]'

  >>> d = Colecao(30)
  >>> d.insere(5)
  >>> d.insere(5)
  >>> d.insere(25)
  >>> d.insere(15)
  >>> d.insere(30)
  >>> d.insere(3)
  >>> d.insere(15)
  >>> d.insere(30)
  >>> d.insere(25)
  >>> d.possuidas()
  '[3, 5, 15, 25, 30]'
  >>> d.repetidas()
  '[5 (2), 15 (2), 25 (2), 30 (2)]'
  
  >>> c.troca_maxima(d)
  >>> c.possuidas()
  '[2, 3, 5, 15, 25]'
  >>> d.possuidas()
  '[2, 3, 5, 15, 25, 30]'
  >>> c.repetidas()
  '[5 (2)]'
  >>> d.repetidas()
  '[5 (2), 15 (2), 30 (2)]'
  
  >>> e = Colecao(3)
  >>> e.insere(1)
  >>> e.insere(2)
  >>> e.insere(3)
  >>> e.possuidas()
  '[1, 2, 3]'
  >>> e.insere(3)
  >>> e.repetidas()
  '[3 (2)]'
  >>> e.insere(4)
  Traceback (most recent call last):
    ...
  ValueError: Número de figurinha inválido
  
  >>> f = Colecao(30)
  >>> f.insere(7)
  >>> f.insere(8)
  >>> f.insere(12)
  >>> f.insere(7)
  >>> f.insere(20)
  >>> f.possuidas()
  '[7, 8, 12, 20]'
  >>> f.repetidas()
  '[7 (2)]'
  
  >>> g = Colecao(30)
  >>> g.insere(10)
  >>> g.insere(8)
  >>> g.insere(12)
  >>> g.insere(7)
  >>> g.insere(20)
  >>> g.possuidas()
  '[7, 8, 10, 12, 20]'
  >>> g.repetidas()
  '[]'
  >>> g.troca_maxima(f)
  >>> f.possuidas()
  '[7, 8, 12, 20]'
  >>> f.repetidas()
  '[7 (2)]'
  >>> g.possuidas()
  '[7, 8, 10, 12, 20]'
  >>> g.repetidas()
  '[]'
  >>> g.remove(20)
  >>> g.remove(10)
  >>> g.remove(8)
  >>> g.possuidas()
  '[7, 12]'
  >>> f.remove(7)
  >>> f.repetidas()
  '[]'
  
  >>> h = Colecao(30)
  >>> h.insere(20)
  >>> h.insere(20)
  >>> h.insere(15)
  >>> h.insere(8)
  >>> h.insere(10)
  >>> h.insere(11)
  >>> h.insere(10)
  >>> h.repetidas()
  '[10 (2), 20 (2)]'
  
  >>> i = Colecao(30)
  >>> i.insere(12)
  >>> i.insere(12)
  >>> i.insere(15)
  >>> i.insere(8)
  >>> i.insere(14)
  >>> i.insere(14)
  >>> i.repetidas()
  '[12 (2), 14 (2)]'
  
  >>> i.troca_maxima(h)
  >>> i.repetidas()
  '[]'
  >>> h.repetidas()
  '[]'
  >>> h.possuidas()
  '[8, 10, 11, 12, 14, 15, 20]'
  >>> i.possuidas()
  '[8, 10, 12, 14, 15, 20]'
  '''

  def __init__(self, quantidade_total: int):
    '''
    Inicializa e define a quantidade maxima de figurinhas da coleção

    o argumento *quantidade_total* deve ser > 0. 
    '''
    self.primeiro: No | None = None
    self.tamanho: int = quantidade_total
      
  def __busca(self, figurinha: int) -> No | None:
    '''
    Retorna o indice da posição da *figurinha* na lista, caso não for
    encontrado o indice retornado é -1
    '''
    i: int = 0
    atual: No | None = self.primeiro
    while atual is not None:
      if atual.dado.n_fig == figurinha:
        return i
      atual = atual.prox
      i += 1
      
    return -1
  
  def insere(self, figurinha: int):
    '''
    Insere *figurinha* na coleção
    '''
    if not (1 <= figurinha <= self.tamanho):
      raise ValueError('Número de figurinha inválido')
  
    nova_figurinha: Figurinha = Figurinha(figurinha)
    novo_no: No = No(nova_figurinha)

    if self.primeiro is None:
      self.primeiro = novo_no 
    else:
      atual: No | None = self.primeiro
      anterior: No | None = None
      
      # Percorre a lista enquanto *figurinha* for maior que o item atual
      # ou ate o final da lista.
      while atual is not None and figurinha > atual.dado.n_fig: 
        anterior = atual
        atual = atual.prox

      if atual is not None and atual.dado.n_fig == figurinha:
        # Caso o numero de *atual.dado.n_fig* for o mesmo numero que *figurinha*, apenas incrementamos + 1 na quantidade do item
        atual.dado.quantidade += 1
      else:
        # Adiciona *figurinha* na colecao
        if anterior is None:
          novo_no.prox = self.primeiro
          self.primeiro = novo_no
        else:
          anterior.prox = novo_no
          novo_no.prox = atual

  def remove(self, figurinha: int):
    '''
    Remove *figurinha* da coleção
    '''
    atual: No | None = self.primeiro
    anterior: No | None = None

    # Percorre a lista enquanto *figurinha* for maior que o item atual
    # ou ate o final da lista.
    while atual is not None and figurinha > atual.dado.n_fig: 
      anterior = atual
      atual = atual.prox

    if atual is not None and atual.dado.n_fig == figurinha:
      # Caso o numero de *atual.dado.n_fig* for o mesmo numero que *figurinha* e *atual.dado.quantidade* for > 1,
      # apenas decrementamos - 1 na quantidade do item
      if atual.dado.quantidade > 1:
        atual.dado.quantidade -= 1
      else:
          # Caso contrário, removemos *figurinha* da coleção
          if anterior is None:
            self.primeiro = atual.prox
          else:
            anterior.prox = atual.prox
    else:
      # A figurinha não está na coleção
      raise ValueError(f"Figurinha {figurinha} não encontrada na coleção.")

  def possuidas(self):
    '''
    Retorna uma string com todas as figurinhas possuidas na coleção
    '''
    figurinhas: list = []
    atual: No | None = self.primeiro
    while atual is not None:
      figurinhas.append(atual.dado.n_fig)
      atual = atual.prox
      
    return str(figurinhas)

  def repetidas(self):
    '''
    Retorna uma string de todas as figurinhas repetidas e quantas são repetidas.
    '''
    repetidas_str: str = '['

    atual: No | None = self.primeiro
    while atual is not None:
      if atual.dado.quantidade > 1:
        if repetidas_str != '[':
          repetidas_str += ', '

        repetidas_str += f'{atual.dado.n_fig} ({atual.dado.quantidade})'

      atual = atual.prox

    return repetidas_str + ']'
  
  def troca_maxima(self, colecao: Colecao):
    '''
    Realiza a troca de figurinhas repetidas entre duas coleções.
    Ambas as coleções devem trocar o mesmo numero de figurinhas.
    
    Requer que as duas coleções possuam o mesmo tamanho.
    '''
    if self.tamanho != colecao.tamanho:
      raise ValueError('Coleções de tamanho diferentes!')

    minha_colecao: list[int] = self.trocaveis(colecao) # Recebe as figurinhas que são trocaveis de *colecao*
    outra_colecao: list[int] = colecao.trocaveis(self) # Recebe as figurinhas que são trocaveis de *self*
      
    tamanho: int = len(minha_colecao) if len(minha_colecao) < len(outra_colecao) else len(outra_colecao)
    
    for i in range(tamanho):
      # Adicionando as figurinhas de *colecao* para a *minha_colecao*
      self.insere(minha_colecao[i])
      colecao.remove(minha_colecao[i])
      
      # Adicionando as figurinhas de *minha_colecao* para a *colecao*
      colecao.insere(outra_colecao[i])
      self.remove(outra_colecao[i])
      
  def n_repetidas(self) -> list[int]:
    '''
    Retorna uma lista com os numeros das *figurinhas* da coleção com quantidade > 1
    
    Exemplos: 
    >>> c = Colecao(30)
    >>> c.insere(3)
    >>> c.insere(5)
    >>> c.insere(2)
    >>> c.insere(5)
    >>> c.insere(15)
    >>> c.insere(2)
    >>> c.n_repetidas()
    [2, 5]

    >>> d = Colecao(30)
    >>> d.insere(5)
    >>> d.insere(5)
    >>> d.insere(25)
    >>> d.insere(15)
    >>> d.insere(30)
    >>> d.insere(3)
    >>> d.insere(15)
    >>> d.insere(30)
    >>> d.insere(25)
    >>> d.n_repetidas()
    [5, 15, 25, 30]
    '''
    lst: list[int] = []
    atual: No | None = self.primeiro
    while atual is not None:
      if atual.dado.quantidade > 1:
        numero_figurinha = atual.dado.n_fig
        lst.append(int(numero_figurinha))
      atual = atual.prox
      
    return lst
  
  def trocaveis(self, colecao: Colecao) -> list[int]:
    '''
    Verifica quais figurinhas são trocaveis

    Exemplos:
    >>> c = Colecao(30)
    >>> c.insere(3)
    >>> c.insere(5)
    >>> c.insere(2)
    >>> c.insere(5)
    >>> c.insere(15)
    >>> c.insere(2)

    >>> d = Colecao(30)
    >>> d.insere(5)
    >>> d.insere(5)
    >>> d.insere(25)
    >>> d.insere(15)
    >>> d.insere(30)
    >>> d.insere(3)
    >>> d.insere(15)
    >>> d.insere(30)
    >>> d.insere(25)

    >>> c.trocaveis(d)
    [25, 30]
    >>> d.trocaveis(c)
    [2]
    '''
    trocaveis: list[int] = []
    figurinhas: list = colecao.n_repetidas()
    
    for i in range(len(figurinhas)):
      if self.__busca(figurinhas[i]) == -1:
        trocaveis.append(figurinhas[i])
        
    return trocaveis