from pickle import TRUE
from Graph import Graph


file = "grafo01.txt"
is_oriented = False

G = Graph(file, is_oriented).graph

print(G)