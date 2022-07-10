import numpy as np

class Node:

    def __init__(self, distance, trace, current_position, tree, visited):
        self.current_position = current_position
        self.tree = tree
        self.visited = visited
        self.visited.append(self.current_position)
        self.trace = trace
        self.trace.append(self.current_position)
        self.distance = self.travel_distance(distance)
        self.sons = self.generate_sons()

    def get_current_position(self):
        return self.current_position[0]

    def get_current_distance(self):
        return self.distance

    def get_trace_value(self):
        return list(self.trace)

    def generate_sons(self):
        sons = []
        j = 0
        for dest in self.tree[self.current_position[0]]:
            if dest != np.inf:
                sons.append([j, dest])
            j += 1
        return sons

    def travel_distance(self, distance):
        if distance != -1:
            return distance + self.current_position[1]
        else: 
            return 0
