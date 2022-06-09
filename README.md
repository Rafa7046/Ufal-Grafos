# Atividade 01 - Planejamento de rota
  # Descrição
    Um robô precisa planejar a menor rota em uma grade de ocupação. Suponha que a grade de ocupação é fornecida como uma matriz com células indicando espaço livre (1) e
    obstáculo (∞). Sabendo que o robô inicia em uma célula específica, e.g. pos = [9, 0], e deseja-se chegar em uma posição destino, e.g. pos_d = [0, 2]. O robô se move
    apenas na horizontal e vertical (não se move na diagonal). Espera-se de retorno uma lista com o caminho.

# Atividade 02 - Definição da central
  # Descrição
    Considere o problema em que existe uma instalação de múltiplos sensores em uma área rural. Apesar esses sensores trabalharem em uma rede mesh distribuída, os
    comandos precisam chegar a uma estação central, onde roda um sistema supervisório que monitora as condições climáticas, a saúde da plantação, entre outras coisas.
    Nesta aplicação, vamos supor 12 locais de instalação de sensor, mas um deles deve ser escolhido como estação central. Usando os conceitos de teoria dos grafos, cada
    local de instalação pode ser considerado um vértice, enquanto o custo de comunicação (ou distância) entre eles são as arestas. Para encontrar o melhor vértice para
    ser o central, podemos aplicar uma otimização considerando dois parâmetros. Tomando um vértice candidato a vértice central, computamos o somatório dos custos para
    chegar nos demais vértices e o custo para o vértice mais distante, para questões de desempate.
