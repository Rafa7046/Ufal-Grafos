import numpy as np

class Graph():

    def __init__(self, file, is_oriented):
        self.read_file(file)
        self.graph = self.get_graph(is_oriented, self.init_matrix())

    def read_file(self, file):
        with open(f"Atividade_2\{file}", "r") as graph:
            test = list(map(int, graph.readline().split()))
            self.vertex, self.edges = test[0], test[1]
            self.path = []
            i = 0
            while i < self.edges:
                self.path.append(list(map(int, graph.readline().split())))
                i+=1

    def init_matrix(self):
        initial_matrix = np.ones((self.vertex, self.vertex)) * np.inf
        np.fill_diagonal(initial_matrix, 0)
        return initial_matrix

    def get_graph(self, is_oriented, initial_matrix):
        if not is_oriented:
            for i in self.path:
                initial_matrix[i[0] - 1][i[1] - 1] = i[2]
                initial_matrix[i[1] - 1][i[0] - 1] = i[2]
        else:
            for i in self.path:
                initial_matrix[i[0] - 1][i[1] - 1] = i[2]
        
        return initial_matrix