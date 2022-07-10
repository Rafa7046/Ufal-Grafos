import shapely.geometry as sp
import numpy as np
import math

class Graph:

    def __init__(self, file):
        self.__read_file(file)
        self.graph = self.__create_visibility_graph()

    def __read_file(self, file):
        with open(f"Atividade_3\{file}", "r") as graph:
            edges = []
            self.ini = list(map(int, graph.readline().split(",")))
            edges.append(self.ini)
            self.end = list(map(int, graph.readline().split(",")))
            edges.append(self.end)
            number_of_obstacles = int(graph.readline())
            obstacles = [0]*number_of_obstacles
            for i in range(number_of_obstacles):
                number_of_edges = int(graph.readline())
                obstacle_edges = []
                for j in range(number_of_edges):
                    edge = list(map(float, graph.readline().split(",")))
                    obstacle_edges.append(edge)
                    edges.append(edge)
                obstacles[i] = sp.polygon.Polygon(obstacle_edges)

        self.edges = np.array(edges)
        self.obstacles = obstacles

    def intersects_polygon(self, path: sp.LineString):
        for polygon in self.obstacles:
            if(path.crosses(polygon) or polygon.covers(path)):
                return True
        return False



    def __create_visibility_graph(self): 
        number_of_edges = len(self.edges)
        graph = []
        for i in range(number_of_edges):
            for j in range(i,number_of_edges):
                path = sp.LineString([self.edges[i], self.edges[j]])
                if(self.intersects_polygon(path) or i == j):
                    continue
                graph.append((i, j, path.length))

        return graph
