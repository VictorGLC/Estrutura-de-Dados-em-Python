class TabelaHash:
  def __init__(self, tamanho):
    self.tamanho = tamanho
    self.tabela = [None] * tamanho

  def hash_function(self, chave):
    return chave % self.tamanho

  def inserir(self, chave, valor):
    index = self.hash_function(chave)
    while self.tabela[index] is not None:
      index = (index + 1) % self.tamanho
    self.tabela[index] = (chave, valor)

  def busca(self, chave):
    index = self.hash_function(chave)
    while self.tabela[index] is not None:
      if self.tabela[index][0] == chave:
        return self.tabela[index][1]
      index = (index + 1) % self.tamanho
    return None

  def remove(self, chave):
    index = self.hash_function(chave)
    while self.tabela[index] is not None:
      if self.tabela[index][0] == chave:
        self.tabela[index] = None
        return
      index = (index + 1) % self.tamanho

  def string(self):
    for i in range(self.tamanho):
      if self.tabela[i] is not None:
        print(f"Índice {i}: {self.tabela[i]}")
      else:
        print(f"Índice {i}: Vazio")


# Exemplo de uso:
tabela = TabelaHash(8)
tabela.inserir(734, "Alice")
tabela.inserir(84, "João")
tabela.inserir(236, "Alfredo")
tabela.inserir(554, "Edson")
tabela.inserir(31, "Davi")
tabela.inserir(141, "Geraldo")

print("Tabela de dispersão:")
tabela.string()

print("\nValor associado a chave 31:", tabela.busca(31))
print("Valor associado a chave 84:", tabela.busca(84))

tabela.remove(734)
print("\nTabela de dispersão após excluir chave 734:")
tabela.string()
