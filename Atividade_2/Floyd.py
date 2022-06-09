import numpy as np
from Graph import Graph

class Floyd():

    def __init__(self, file, is_oriented):
        self._graph = Graph(file, is_oriented).graph
        self.floyd_matrix = self.gerar_tabela_dist()

    @property
    def graph(self):
        return self._graph.copy()

    def gerar_tabela_dist(self):
        size = self.graph[0].size
        for current_matrix in range(size):
            if current_matrix == 0:
                old = self.graph
            else:
                old = new.copy()
            new = self.ini_new_matrix(old, size, current_matrix)
            for i in range(size):
                for j in range(size):
                    if new[i][j] == -1:
                        if old[i][j] > new[i][current_matrix] + new[current_matrix][j]:
                            new[i][j] = new[i][current_matrix] + new[current_matrix][j]
                        else:
                            new[i][j] = old[i][j]
        
        return new


    def ini_new_matrix(self, old, size, current_matrix):
        new = np.ones((size, size)) * - 1
        new[current_matrix] = old[current_matrix].copy()
        new[:, current_matrix] = old[:, current_matrix].copy()
        np.fill_diagonal(new, np.diagonal(old).copy())
        return new
