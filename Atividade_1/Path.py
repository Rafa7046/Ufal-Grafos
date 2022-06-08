from Map import Map

class Path():
    
    def __init__(self, time, trace, current_position, occupancy, visited):
        self.current_position = current_position
        self.occupancy = occupancy
        self.visited = visited
        self.visited.append(self.current_position)
        self.trace = trace
        self.trace.append(self.current_position)
        self.time = self.travel_time(time)
        self.sons = self.paths()

    def get_current_position(self):
        return self.current_position

    def get_current_time(self):
        return self.time

    def get_trace_value(self):
        return list(self.trace)

    def paths(self):
        map = Map(self.occupancy)
        sons = map.find_paths(self.current_position, self.visited)
        return sons

    def travel_time(self, time):
        if time != -1:
            return time + self.occupancy[self.current_position[0]][self.current_position[1]]
        else: 
            return 0
