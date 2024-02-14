from __future__ import annotations

class Figurinha:
  def __init__(self, figurinha):
    self.n_fig: int = figurinha
    self.quantidade: int = 1

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
    self.tam: int = 0
    self.tam_max: int = quantidade_total
    self.elementos: list[Figurinha | None] = [None] * quantidade_total

  def __busca(self, figurinha: int) -> int:
    '''
    Retorna o indice da posição da *figurinha* na lista, caso não for
    encontrado o indice retornado é -1
    '''
    for i in range(self.tam):
      if self.elementos[i].n_fig == figurinha:
        return i
    return -1

  def vazia(self) -> bool:
    '''
    Retorna True se a lista estiver vazia e retorna False se a lista não estiver vazia
    '''
    return self.tam == 0

  def insere(self, figurinha: int):
    '''
    Insere *figurinha* na coleção
    '''
    if not (1 <= figurinha <= self.tam_max):
      raise ValueError('Número de figurinha inválido')

    indice_existente: int = self.__busca(figurinha)

    if indice_existente != -1:
      # Incrementa a quantidade se *figurinha* já existe
      self.elementos[indice_existente].quantidade += 1
    else:
      # Caso contrário, adicionamos *figurinha* na lista
      nova_figurinha: Figurinha = Figurinha(figurinha)

      if self.vazia():
        self.elementos[self.tam] = nova_figurinha
      else:
        i: int = 0
        # Percorre a lista até achar o indice onde *figurinha* é menor que o sucessor
        while self.tam > i and figurinha > self.elementos[i].n_fig: 
            i += 1

        # Desloca os elementos à direita para abrir espaço para a nova figurinha
        for j in range(self.tam, i, -1):
            self.elementos[j] = self.elementos[j - 1]

        # Insere a nova figurinha na posição correta
        self.elementos[i] = nova_figurinha

      self.tam += 1
      
  def remove(self, figurinha: int):
    '''
    Remove *figurinha* da coleção
    '''
    if self.vazia():
      raise ValueError('Coleção vazia')

    indice_existente: int = self.__busca(figurinha)
    
    # Se *figurinha* existir na lista
    if indice_existente != -1:
      if self.elementos[indice_existente].quantidade > 1:
        # Se há mais de uma figurinha, apenas decrementa a quantidade
        self.elementos[indice_existente].quantidade -= 1
      else:
        # Se há apenas uma figurinha, remove o elemento da lista e desloca os elementos à esquerda
        for i in range(indice_existente, self.tam):
            self.elementos[i] = self.elementos[i + 1]

        self.tam -= 1
    else:
      raise ValueError('Figurinha não encontrada na coleção')

  def possuidas(self) -> str:
    '''
    Retorna uma string com todas as figurinhas possuidas na coleção.
    '''
    figurinhas: list[int] = []
    for i in range(self.tam):
      if self.elementos[i] is not None:
        figurinhas.append(self.elementos[i].n_fig)
        
    return str(figurinhas)

  def repetidas(self) -> str:
    '''
    Retorna uma string de todas as figurinhas repetidas e quantas são repetidas.
    '''
    repetidas_str: str = '['

    for i in range(self.tam):
      if self.elementos[i].quantidade > 1:
        if repetidas_str != '[':
          repetidas_str += ', '

        repetidas_str += f'{self.elementos[i].n_fig} ({self.elementos[i].quantidade})'

    return repetidas_str + ']'
  
  def troca_maxima(self, colecao: Colecao):
    '''
    Realiza a troca de figurinhas repetidas entre duas coleções.
    Ambas as coleções devem trocar o mesmo numero de figurinhas.

    Requer que as duas coleções possuam o mesmo tamanho
    '''
    if self.tam_max != colecao.tam_max:
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
    Ex: 
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
    lst = []
    for i in range(self.tam):
      if self.elementos[i].quantidade > 1:
        numero_figurinha = self.elementos[i].n_fig
        lst.append(int(numero_figurinha))
        
    return lst
  
  def trocaveis(self, colecao: Colecao) -> list[int]:
    '''
    Verifica quais figurinhas são trocaveis

    Ex:
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
    figurinhas: list[int] = colecao.n_repetidas()
    
    for i in range(len(figurinhas)):
      if self.__busca(figurinhas[i]) == -1:
        trocaveis.append(figurinhas[i])
        
    return trocaveis
    