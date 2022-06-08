import numpy as np
from Robot import Robot

def main(robot_pos_c, robot_pos_d, occupancy):

    robot = Robot(robot_pos_c, robot_pos_d, occupancy)
    path = robot.robot_path()

    print("======================================================================================================")
    print(f"O melhor caminho para o Robô é o {path[0]} \n e ele levará um tempo de {path[1]:.2f} segundos.")
    print("======================================================================================================")

robot_pos_c = [9, 0] # Robot current position
robot_pos_d = [0, 2] # Robot desired position

# Aplicação básica

# occupancy = np.ones((10, 10))
# occupancy[0:5, 0] = np.inf
# occupancy[5, 0:5] = np.inf
# occupancy[5:8, 5] = np.inf
# occupancy[0:3, 5:8] = np.inf
# occupancy[7:9, 3] = np.inf
# occupancy[5:10, 8] = np.inf

# Considerando terreno

occupancy = 10 * np.random.rand(10, 10)
occupancy[0:5, 0] = np.inf
occupancy[5, 0:5] = np.inf
occupancy[5:8, 5] = np.inf
occupancy[0:3, 5:8] = np.inf
occupancy[7:9, 3] = np.inf
occupancy[5:10, 8] = np.inf

main(robot_pos_c, robot_pos_d, occupancy)
