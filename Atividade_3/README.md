# Atividade 03 - Grafo de visibilidade de robô
  # Bibliotecas adicionais
    Fora a biblioteca numpy foi utilizada a shapely, será necessário instalar ambas para rodar o código

  # Descrição
    Considere o problema de planejamento de caminho para veículos autônomos. Existem formas diferentes de representar o mapa em que o algoritmo de planejamento deve
    atuar. Agora vamos trabalhar com uma representação topológica do ambiente. Podemos montar esse tipo de mapa, em um espaço poligonal, com uma técnica conhecida como
    Grafo de Visibilidade. Dizemos que existe aresta entre dois vértices se houver visada direta entre eles, ou seja, se montamos uma linha reta entre os dois pontos,
    não há obstáculo, o robô se mantém no espaço de configurações livres de colisão.
    O grafo resultante serve como roadmap, não só para ir de  qstart  para  qgoal , mas permite planejar caminhos do veículo para outras regiões do mapa. Tudo isso
    usando técnicas de teoria dos grafos. Sabendo que o veículo sempre inicia em uma certa posição, podemos explorar algoritmos de busca ainda mais eficientes na
    estrutura de árvore. Pretende-se então descobrir qual a árvore que passa por todos os vértices e o custo total é mínimo. Esse problema pode ser trabalhado com os
    algoritmos de Kruskal e Prim, foi implementado ambos algoritmos. Caso o robô inicie em um local não contemplado com um vértice, podemos fazer um caminho até o
    vértice mais próximo e de lá seguir o roadmap para o local desejado. Portanto, precisamos de uma rotina que descubra qual o vértice do grafo mais próximo dado um
    ponto no plano.
