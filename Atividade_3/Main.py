from Graph import Graph
from Kruskal import Kruskal
from Prim import Prim

graph = Graph("mapa.txt")
kruskal = Kruskal(graph).mst
prim = Prim(graph).mst
