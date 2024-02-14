# Primeiro Trabalho de Implementação - Gerenciamento de Coleções de Figurinhas

Durante a Copa do Mundo de futebol, muitos admiradores desse esporte se dedicam a colecionar as figurinhas da copa. Como bom observador, você já notou que existe uma certa confusão quando as pessoas se reúnem para trocar figurinhas. O problema, na sua visão, é que é difícil para um colecionador encontrar as pessoas certas com quem ele possa trocar as figurinhas e também é difícil manipular as figurinhas, em especial, as repetidas.

Você imagina que seja possível criar uma plataforma onde os usuários possam gerenciar os álbuns e encontrar pessoas para trocar figurinhas. Você imagina o cenário em que um grupo de pessoas se reúne em um local, e o seu aplicativo mostra na tela de cada telefone a quantidade de pessoas no local, quem tem as figurinhas repetidas que cada usuário precisa, quantas trocas são possíveis fazer, etc.

Você sabe que chegar nesse resultado pode levar um tempo, mas você também sabe que é possível começar fazendo as estruturas e operações básicas que serão necessárias para manter as coleções. Como as figurinhas são enumeradas (1, 2, 3, ...), o seu trabalho é manter uma coleção ordenada de números, com o detalhe de que cada número pode aparecer mais que uma vez na coleção (figurinhas repetidas).

Para uma coleção, você identificou as seguintes operações:

- Criação de uma coleção com a quantidade de figurinhas (número de figurinhas total do álbum).
- Inserção de uma figurinha.
- Remoção de uma figurinha.
- Geração de uma string com as figurinhas presentes sem considerar as repetições (ex "[4, 10, 25]").
- Geração de uma string com as figurinhas repetidas (ex "[12 (1), 60 (2)]", 1 repetida da 12 e 2 repetidas da 60).
- Troca máxima entre duas coleções (Suponha que o programa identificou duas pessoas para fazerem a troca de figurinhas, a primeira tem 6 figurinhas repetidas que a segunda não tem e a segunda tem 8 figurinhas que a primeira não tem. Então, essa operação tem que transferir 6 figurinhas da primeira para a segunda pessoa e 6 figurinhas da segunda para a primeira. As figurinhas que serão transferidas são escolhidas por ordem).

Agora você precisa trabalhar!

1. Faça a especificação de um TAD para representar coleções de figurinhas com as operações identificadas acima.
2. Faça uma implementação usando arranjo estático.
3. Faça uma implementação usando encadeamento.