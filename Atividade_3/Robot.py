from Prim import Prim
from Kruskal import Kruskal
from Node import Node
import numpy as np
import math as mt

class Robot():

    def __init__(self, file, type_of_tree, start, end):
        mst = Kruskal(file) if type_of_tree else Prim(file)
        self.tree = self.create_matrix(mst.mst)
        self.edges = mst.edges
        self.start, self.end = self.find_closer_edge(np.array([start, end]) , np.array(self.edges))
        self.border = [Node(-1, [], self.start, self.tree, [])]

    def create_matrix(self, tree):
        matrix = np.ones((15, 15))*np.inf
        for node in tree:
            matrix[node[0]][node[1]] = node[2]
            matrix[node[1]][node[0]] = node[2]
        return matrix

    def find_closer_edge(self, coords, edges):
        new_edges = []
        for coord in coords:
            closer_distance = np.inf
            for edge in edges:
                if np.array_equal(coord, edge): 
                    closer_edge = coord
                    break
                distance = mt.sqrt(mt.pow(coord[0]-edge[0], 2) + mt.pow(coord[1]-edge[1], 2))
                if distance < closer_distance:
                    closer_distance = distance
                    closer_edge = edge
            new_edges.append([np.where(edges == closer_edge)[0][0]])
        
        return new_edges

    def find_min(self):
        min = (self.border[0]).get_current_distance()
        index = 0
        for i in range(len(self.border)):
            if self.border[i].get_current_distance() < min:
                min = self.border[i].get_current_distance()
                index = i
        return self.border[index]

    def robot_path(self):
        while len(self.border) != 0:
            node = self.find_min()
            if node.get_current_position() == self.end[0]:
                    return self.format_result(node.trace, node.distance)
            for son in node.sons:
                new_son = Node(node.get_current_distance(), node.get_trace_value(), son, self.tree, node.visited)
                self.border.append(new_son)
            self.border.remove(node)

    def format_result(self, trace, distance):
        start = self.edges[self.start[0]]
        end = self.edges[self.end[0]]
        path = []
        for node in trace:
            path.append((self.edges[node[0]][0], self.edges[node[0]][1]))

        return ((start[0], start[1]), (end[0], end[1]), path, distance)