import numpy as np

class Map:

    def __init__(self, occupancy) :
        self.occupancy = occupancy

    def find_paths(self, current_position, visited):
        paths = []

        next_i = current_position[0] + 1
        previus_i = current_position[0] - 1
        next_j = current_position[1] + 1
        previus_j = current_position[1] - 1

        if (next_i <= 9 and self.occupancy[next_i][current_position[1]] != np.inf):
            paths.append([next_i, current_position[1]])
        if (previus_i >= 0 and self.occupancy[previus_i][current_position[1]] != np.inf):
            paths.append([previus_i, current_position[1]])
        if (next_j <= 9 and self.occupancy[current_position[0]][next_j] != np.inf):
            paths.append([current_position[0], next_j])
        if (previus_j >= 0 and self.occupancy[current_position[0]][previus_j] != np.inf):
            paths.append([current_position[0], previus_j])

        for path in paths:
            if path in visited:
                paths.remove(path)

        return paths
        