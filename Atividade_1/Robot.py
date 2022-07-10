from numpy import empty
from Path import Path

class Robot():

    def __init__(self, initial_position, final_position, occupancy):
        self.initial_position = initial_position
        self.final_position = final_position
        self.occupancy = occupancy
        self.border = [Path(-1, [], initial_position, self.occupancy, [])]

    def robot_path(self):
        while self.border is not empty:
            path = self.find_min()
            if path.get_current_position() == self.final_position:
                    return (path.trace, path.time)
            for son in path.sons:
                new_son = Path(path.get_current_time(), path.get_trace_value(), son, self.occupancy, path.visited)
                self.border.append(new_son)
            self.border.remove(path)

    def find_min(self):
        min = (self.border[0]).get_current_time()
        index = 0
        for i in range(len(self.border)):
            if self.border[i].get_current_time() < min:
                min = self.border[i].get_current_time()
                index = i
        return self.border[index]
