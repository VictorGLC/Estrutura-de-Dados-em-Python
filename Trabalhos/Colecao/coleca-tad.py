from __future__ import annotations

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
    raise NotImplemented

  def insere(self, figurinha: int):
    '''
    Insere *figurinha* na coleção
    '''
    raise NotImplemented

  def remove(self, figurinha: int):
    '''
    Remove *figurinha* da coleção
    '''
    raise NotImplemented

  def possuidas(self):
    '''
    Retorna uma string com todas as figurinhas possuidas na coleção.
    '''
    raise NotImplemented

  def repetidas(self):
    '''
    Retorna uma string de todas as figurinhas repetidas e quantas são repetidas.
    '''
    raise NotImplemented
  
  def troca_maxima(self, colecao: Colecao):
    '''
    Realiza a troca de figurinhas repetidas entre duas coleções.
    Ambas as coleções devem trocar o mesmo numero de figurinhas.

    Requer que as duas coleções possuam o mesmo tamanho.
    '''
    raise NotImplemented