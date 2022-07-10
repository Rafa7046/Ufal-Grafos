class Kruskal:

    def __init__(self, graph):
        self.graph = sorted(graph.graph, key = lambda graph:graph[2])
        self.kruskal_array = [0]*len(graph.edges)
        self.mst = []
        self.kruskal()

    def find(self, node):
        if self.kruskal_array[node] == 0:
            return node
        else:
            temp = self.find(self.kruskal_array[node])
            self.kruskal_array[node] = temp
            return temp

    def union(self, a, b, c):
        temp_a = a
        temp_b = b
        a = self.find(a)
        b = self.find(b)
        if a != b:
            self.mst.append([temp_a, temp_b, c])
            if self.kruskal_array[a] < self.kruskal_array[b]:
                self.kruskal_array[a] = self.kruskal_array[a] + self.kruskal_array[b]
                self.kruskal_array[b] = a
            else:
                self.kruskal_array[b] = self.kruskal_array[a] + self.kruskal_array[b]
                self.kruskal_array[a] = b

    def kruskal(self):
        for a, b, c in self.graph:
            self.union(a, b, c)