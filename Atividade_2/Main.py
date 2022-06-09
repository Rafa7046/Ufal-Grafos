from Station import Station

def main(file, is_oriented):
    central_station = Station(file, is_oriented).station

    print(f"O melhor local para ser a estação central é a {central_station}.")

    return

# As variáveis abaixo se referenciam ao grafo que sera analizado e se ele é um grafo orientado ou não,
# necessário configura-las corretamente para o que código funcione como o esperado.
# A variável "file" necessita apenas do nome do arquivo dado que ele esteja do diretório "atividade_2", e a sua extensão.
# A variável "is_oriented" é um booleano que indica se o grafo é orientado ou não.

file = "grafo01.txt"
is_oriented = False

main(file, is_oriented)