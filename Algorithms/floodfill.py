import API
from helper_func import  *
import numpy as np

# List used to store temporary values of neighbouring cells
temp = [0, 0, 0, 0] # [N, S, W, E]
# Array used to store walls
wall_map = [[None for _ in range(16)] for _ in range(16)]

goals = [(API.mazeWidth() // 2 - 1, API.mazeHeight() // 2 - 1),
        (API.mazeWidth() // 2 - 1, API.mazeHeight() // 2),
        (API.mazeWidth() // 2, API.mazeHeight() // 2 - 1),
        (API.mazeWidth() // 2, API.mazeHeight() // 2)]

# Creating initial map of the maze (each cell is given the value of the manhattan distance from the target position)
maze_map = np.ones((16,16))
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
    x, y = cell
    return [int(maze_map[x][y+1]), 
            int(maze_map[x][y-1]),
            int(maze_map[x-1][y]), 
            int(maze_map[x+1][y])]
    
def update_walls(cell, heading):
    # Relative walls reported by the API
    front = API.wallFront()
    right = API.wallRight()
    back  = API.wallBack()
    left  = API.wallLeft()

    # Absolute wall order: [N, S, W, E]
    walls = [0, 0, 0, 0]

    if heading == 'N':
        walls = [
            int(front),   
            int(back),    
            int(left),    
            int(right)    
        ]

    elif heading == 'E':
        walls = [
            int(left),    
            int(right),   
            int(back),   
            int(front)    
        ]

    elif heading == 'S':
        walls = [
            int(back),    
            int(front),   
            int(right),   
            int(left)     
        ]

    elif heading == 'W':
        walls = [
            int(right),   
            int(left),    
            int(front),   
            int(back)     
        ]
    x, y = cell
    wall_map[x][y] = walls
    return walls

def get_cell_value(cell):
    x, y = cell
    return maze_map[x][y]

def update_map():
    pass

def get_target_direction(cell, temp):
    x, y = cell
    available_cells = []
    target_direction = None
    walls = wall_map[x][y]
    if get_cell_value(cell) <= min(temp):
        # no neighbouring cell with smaller value
        log("no neighbor, update values")
        update_map()
    else:
        for i, cell in enumerate(temp):
            if walls[i] == 0:
                available_cells.append(i)
                log("no. wall")
        # available cell with minimum value 
        target_cell = min(available_cells)
        if target_cell == 0:
            target_direction = 'N'
        elif target_cell == 1:
            target_direction = 'S'
        elif target_cell == 2:
            target_direction = 'W'
        elif target_cell == 3:
            target_direction = 'E'
        return target_direction
    
def move_in(target_direction):
    heading = get_heading()
    if heading == target_direction:
        moveForward()
    

def main():
    while get_position() not in goals:
        active_cell = (0, 0)
        maze_info()
        # Initialise cell values 
        display_cell_value(maze_map)
        # update wall map
        update_walls(active_cell, get_heading())
        # get value of the neigbouring cells
        temp = get_neighbour_vals(active_cell)
        # move to neighboring node
        target_direction = get_target_direction(active_cell, temp))
        move_in(target_direction)
        log(temp)
        log(wall_map)
    #check_available_node(temp)
    

if __name__ == "__main__":
    main()
