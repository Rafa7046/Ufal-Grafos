from Robot import Robot
import time
from random import randint, uniform


# As variáveis pos_inicial, pos_final se referenciam a posição inicial do robo onde cada uma é um array de float com a posição de x e y
# necessário configura-las corretamente para o que código funcione como o esperado.
# A variável "file" necessita apenas do nome do arquivo dado que ele esteja do diretório "atividade_3", e a sua extensão.
# A variável "type_of_tree" é um booleano que indica qual mst usar, onde 0 para Prim e 1 Kruskal.

file = "mapa.txt"
type_of_tree = randint(0, 1)
pos_inicial = [uniform(0, 12), uniform(0, 12)]
pos_final = [uniform(0, 12), uniform(0, 12)]

def prints(path, inicio, fim, type_of_tree):
    print(f"O melhor caminho partindo do vértice {path[0]} para o vértice {path[1]} é pelos vértices:", end=" [")
    for move in path[2]:
        if move == path[2][-1]:
            print(f"{move}]", end=", ")
            break
        print(f"{move}", sep=', ', end=", ")
    print(f"tem um custo de {path[3]}", end=". ")
    tree = "Kruskal" if type_of_tree else "Prim"
    print(f"utlizando o algoritmo de {tree} para gerar a mst", end=". ")
    print(f"E o tempo de execução do código foi de {fim - inicio} segundos")

def main(file, type_of_tree, pos_inicial, pos_final):
    inicio = time.time()
    robot = Robot(file, type_of_tree, pos_inicial, pos_final)
    path = robot.robot_path()
    fim = time.time()
    prints(path, inicio, fim, type_of_tree)

main(file, type_of_tree, pos_inicial, pos_final)





