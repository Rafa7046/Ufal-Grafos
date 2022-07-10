from heapq import heappop, heappush
from Graph import Graph

class Prim:
    def __init__(self, file):
        graph = Graph(file)
        self.edges = graph.edges
        self.graph = graph.graph
        self.vertices = len(graph.edges)
        self.mst = []
        self.prim()

    def prim(self):
        graph = self.graph
        edges = [[] for _ in range(self.vertices)]
        for edge in graph:
            heappush(edges[edge[0]], (edge[2], edge[1]))
            heappush(edges[edge[1]], (edge[2], edge[0]))
        visited = set()
        cost, dest = 0, 1
        while len(visited) < self.vertices:
            smallest_edge = 0
            for vertex in visited:
                while len(edges[vertex]) > 0 and edges[vertex][0][dest] in visited:
                    heappop(edges[vertex])
                
                if len(edges[vertex]) == 0: continue

                if len(edges[smallest_edge]) == 0 or edges[vertex][0][cost] < edges[smallest_edge][0][cost]:
                    smallest_edge = vertex

            edge = heappop(edges[smallest_edge])
            self.mst.append((smallest_edge, edge[dest], edge[cost]))
            visited.add(smallest_edge)
            visited.add(edge[dest])
     