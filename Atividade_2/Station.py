import numpy as np
from Floyd import Floyd

class Station():

    def __init__(self, file, is_oriented):
        self.distance_matrix = Floyd(file, is_oriented).gerar_tabela_dist()
        self.station = self.central_station()

    def dist_sum_vec(self):
        self.sum_vec = []
        for line in self.distance_matrix:
            self.sum_vec.append(np.sum(line))

    def max_dist_vec(self):
        self.max_vec = []
        for line in self.distance_matrix:
            self.max_vec.append(np.amax(line))

    def central_station(self):
        self.dist_sum_vec()
        self.max_dist_vec()
        min_value = np.amin(self.sum_vec)
        min_index = np.where(self.sum_vec == min_value)[0]
        if len(min_index) > 1:
            min_value = self.max_vec[min_index[0]]
            station = min_index[0]
            for i in min_index:
                if self.max_vec[i] < min_value:
                    min_value = self.max_vec[i]
                    station = i
        else:
            station = min_index
            
        return station+1

