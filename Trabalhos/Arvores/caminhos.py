from arvore_binaria import *

def caminhos_maximos_aux(no: No, caminho_atual: list[int], altura_restante: int, caminhos: list[list[int]]):
    '''
    Percorre todos os ramos da árvore para encontrar todos os caminhos máximos possíveis e os adiciona a *caminhos*

    Exemplo:
    >>> arvore = Arvore()
    >>> arvore.insere(Item(1))
    >>> arvore.insere(Item(2))
    >>> arvore.insere(Item(3))
    >>> caminhos = []
    >>> caminhos_maximos_aux(arvore.raiz, [], 3, caminhos)
    >>> caminhos
    [[1, 2, 3]]
    
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
    >>> caminhos = []
    >>> caminhos_maximos_aux(t.raiz, [], 4, caminhos)
    >>> caminhos
    [[2, 8, 3, 4], [2, 3, 5, 2]]
    
    >>> a = Arvore()
    >>> a.insere(Item(7))
    >>> a.insere(Item(5))
    >>> a.insere(Item(10))
    >>> a.insere(Item(4))
    >>> a.insere(Item(15))
    >>> a.insere(Item(14))
    >>> a.insere(Item(12))
    >>> a.insere(Item(25))
    >>> a.insere(Item(22))
    >>> caminhos = []
    >>> caminhos_maximos_aux(a.raiz, [], 5, caminhos)
    >>> caminhos
    [[7, 10, 15, 14, 12], [7, 10, 15, 25, 22]]
    '''
    if no is None:
        return
    caminho_atual.append(no.dado.chave)
    if altura_restante == 1:
        caminhos.append(caminho_atual[:])
    else:
        caminhos_maximos_aux(no.esq, caminho_atual[:], altura_restante - 1, caminhos)
        caminhos_maximos_aux(no.dir, caminho_atual[:], altura_restante - 1, caminhos)
        
def caminhos_maximos(arvore: Arvore) -> list[list[int]]:
    '''
    Retorna uma lista com todos os caminhos máximos da árvore.

    Exemplo:
    
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
    >>> caminhos_maximos(t)
    [[2, 8, 3, 4], [2, 3, 5, 2]]
    
    >>> a = Arvore()
    >>> a.insere(Item(7))
    >>> a.insere(Item(5))
    >>> a.insere(Item(10))
    >>> a.insere(Item(4))
    >>> a.insere(Item(15))
    >>> a.insere(Item(14))
    >>> a.insere(Item(12))
    >>> a.insere(Item(25))
    >>> a.insere(Item(22))
    >>> caminhos_maximos(a)
    [[7, 10, 15, 14, 12], [7, 10, 15, 25, 22]]
    >>> a.insere(Item(4))
    >>> a.insere(Item(3))
    >>> a.insere(Item(1))
    >>> caminhos_maximos(a)
    [[7, 5, 4, 3, 1], [7, 10, 15, 14, 12], [7, 10, 15, 25, 22]]
    
    >>> b = Arvore()
    >>> b.insere(Item(2))
    >>> b.insere(Item(1))
    >>> b.insere(Item(3))
    >>> caminhos_maximos(b)
    [[2, 1], [2, 3]]
    '''
    caminhos = []
    altura_arvore = arvore.altura(arvore.raiz)
    caminhos_maximos_aux(arvore.raiz, [], altura_arvore, caminhos)
    return caminhos