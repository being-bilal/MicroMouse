import API
from helper_func import log, maze_info, solver_info
import numpy as np

# List used to store temporary values of neighbouring cells
temp = [0, 0, 0, 0]

# Creating initial map of the maze (each cell is given the value of the manhattan distance from the target position.)
maze_map = np.ones((16,16))
goals = [(API.mazeWidth() // 2 - 1, API.mazeHeight() // 2 - 1),
        (API.mazeWidth() // 2 - 1, API.mazeHeight() // 2),
        (API.mazeWidth() // 2, API.mazeHeight() // 2 - 1),
        (API.mazeWidth() // 2, API.mazeHeight() // 2)]

for goal in goals:
    x, y = goal 
    maze_map[x][y] = 0
    
for i, row in enumerate(maze_map):
        for j, cell in enumerate(row):
            # d = |x₁ - x₂| + |y₁ - y₂|
            x1, y1 = i, j
            distance = []
            for goal in goals:
                x2, y2 = goal
                d = abs(x1 - x2) + abs(y1 - y2)
                distance.append(d)
            min_distance = min(distance)
            maze_map[x1][y1] = min_distance
            distance.clear()


def display_cell_value(map):
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            cell_value = int(cell)
            API.setText(i, j, cell_value)
            
def get_neighbour_vals(cell):
    temp = []

def main():
    active_cell = (0, 0)
    log("Running...")
    maze_info()
    display_cell_value(maze_map)
    temp = get_neighbour_vals(active_cell)

if __name__ == "__main__":
    main()
