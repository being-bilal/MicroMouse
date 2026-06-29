import API
from helper_func import  *
import numpy as np

# List used to store temporary values of neighbouring cells
temp = [0, 0, 0, 0] # [N, S, W, E]
# Array used to store walls
wall_map = [[None for _ in range(16)] for _ in range(16)]
# List of visited nodes
visited = []

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
    queue = []
    
    # Seed the queue with all visited cells that need re-evaluation
    for cell in visited:
        x, y = cell
        if wall_map[x][y] is None:
            continue
        walls = wall_map[x][y]
        neighbors = get_neighbour_vals(cell)
        accessible = [neighbors[i] for i in range(4) if walls[i] == 0]
        if not accessible:
            continue
        correct_val = min(accessible) + 1
        if maze_map[x][y] != correct_val:
            maze_map[x][y] = correct_val
            queue.append(cell)

    # BFS propagation
    while queue:
        cx, cy = queue.pop(0)
        walls = wall_map[cx][cy]
        if walls is None:
            continue

        # Check each accessible neighbor of this cell
        neighbor_coords = [
            (cx, cy + 1),  # N
            (cx, cy - 1),  # S
            (cx - 1, cy),  # W
            (cx + 1, cy),  # E
        ]

        for i, (nx, ny) in enumerate(neighbor_coords):
            if walls[i] == 1:
                continue
            if not (0 <= nx < 16 and 0 <= ny < 16):
                continue

            n_walls = wall_map[nx][ny]
            if n_walls is None:
                continue

            # Recompute what this neighbor's value should be
            n_neighbors = get_neighbour_vals((nx, ny))
            n_accessible = [n_neighbors[j] for j in range(4) if n_walls[j] == 0]
            if not n_accessible:
                continue

            correct_val = min(n_accessible) + 1
            if maze_map[nx][ny] != correct_val:
                maze_map[nx][ny] = correct_val
                queue.append((nx, ny))

    display_cell_value(maze_map)

def get_target_direction(cell, temp):
    x, y = cell
    available_cell_index = []
    target_direction = None
    walls = wall_map[x][y]    
    for i, cell in enumerate(temp):
        if walls[i] == 0:
            available_cell_index.append(i)
    # available cell with minimum value 
    log(temp)
    available_cells = [temp[i] for i in available_cell_index]
    if maze_map[x][y] <= min(available_cells):
        # no neighbouring cell with smaller value
        log("no neighbor, update values")
        update_map()
    
    target_cell = min(available_cell_index, key=lambda i: temp[i])
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
    directions = ['N', 'E', 'S', 'W']
    current = directions.index(heading)
    target = directions.index(target_direction)
    diff = (target - current) % 4
    if diff == 0:
        moveForward()
    elif diff == 1:
        turnRight()
        moveForward()
    elif diff == 2:
        pass # Reverse motion is not allowed 
    elif diff == 3:
        turnLeft()
        moveForward()

def main():
    while get_position() not in goals:
        active_cell = get_position()
        if active_cell not in visited:
            # Initialise cell values 
            display_cell_value(maze_map)
            # update wall map
            update_walls(active_cell, get_heading())
            # get value of the neigbouring cells
            temp = get_neighbour_vals(active_cell)
            # Get the target direction of the next node
            target_direction = get_target_direction(active_cell, temp)
            # move in that direction 
            move_in(target_direction)
            visited.append(active_cell)
        else:
            pass    

if __name__ == "__main__":
    main()
