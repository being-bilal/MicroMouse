import API
from helper_func import *
import numpy as np
from BFS import BFS

if API.mazeWidth() == API.mazeHeight():
    length = API.mazeWidth()
elif API.mazeWidth() > API.mazeHeight():
    length = API.mazeWidth()
else:
    length = API.mazeHeight()

# center four cells are the goal cells for the maze
goal = [(API.mazeWidth() // 2 - 1, API.mazeHeight() // 2 - 1),
        (API.mazeWidth() // 2 - 1, API.mazeHeight() // 2),
        (API.mazeWidth() // 2, API.mazeHeight() // 2 - 1),
        (API.mazeWidth() // 2, API.mazeHeight() // 2)]

def move_to_connected_node(current_node, next_node):
    x1, y1 = current_node
    x2, y2 = next_node
    distance_traveled = 0 
    while get_position() != next_node:
        if x1 == x2:
            if y1 < y2:
                while get_heading() != "N":
                    turnLeft()
                while get_position() != next_node:
                    moveForward()
                    distance_traveled += 1
            else:
                while get_heading() != "S":
                    turnLeft()
                while get_position() != next_node:
                    moveForward()
                    distance_traveled += 1
        elif y1 == y2:
            if x1 < x2:
                while get_heading() != "E":
                    turnLeft()
                while get_position() != next_node:
                    moveForward()
                    distance_traveled += 1
            else:
                while get_heading() != "W":
                    turnLeft()
                while get_position() != next_node:
                    moveForward()
                    distance_traveled += 1
    return distance_traveled


def main():
    # Using BFS to completely traverse the maze and build a graph representation of the maze
    # Node : every junction, turn, and dead end in the maze
    nodes, wall_map = BFS()
    node_weight = {}
    edge_weight = {}
    parents = {}
    # finding neighbors for each node 
    # Neighbors are defined as the closest node in each direction without a wall in between 
    graph = {}
    for node in nodes:
        x, y = node
        neighbors = []
        if (x, y) in wall_map:
            walls = wall_map[(x, y)]
            
        for i in range(1, length + 1):
            if 'n' not in walls and (x, y + i) in nodes:
                neighbors.append((x, y + i))
                break
            
        for i in range(1, length + 1):
            if 'e' not in walls and (x + i, y) in nodes:
                neighbors.append((x + i, y))
                break

        for i in range(1, length + 1):
            if 's' not in walls and (x, y - i) in nodes:
                neighbors.append((x, y - i))
                break

        for i in range(1, length + 1):
            if 'w' not in walls and (x - i, y) in nodes:
                neighbors.append((x - i, y))
                break
        graph[node] = neighbors
    
    # Assigning weights to the nodes in the graph
    # Initial weight : 0 for the initial node, infinity for all other nodes
    for node in graph:
        if node == (0, 0):
            node_weight[node] = 0
        else:
            node_weight[node] = float('inf')
    
    # Assigning weights to the edges in the graph
    for node in graph:
        for neighbor in graph[node]:
            x1, y1 = node
            x2, y2 = neighbor
            weight = abs(x1 - x2) + abs(y1 - y2)
            edge_weight[(node, neighbor)] = weight

    # sorting graph
    graph = {
    node: sorted(neighbors, key=node_sort_key)
    for node, neighbors in sorted(graph.items(), key=lambda item: node_sort_key(item[0]))
    }
    log("Graph: {}".format(graph))
    log("Node Weights: {}".format(node_weight))
    log("Edge Weights: {}".format(edge_weight))
    
    
    # Djikstra Algorithm Application 
    # start moving through the graph and updating the node weights
    if get_position() == (0, 0):
        for node in graph:
            for i in graph[node]:
                log(i)
            """
            d = move_to_connected_node((0, 0), i)
            if d < node_weight[i]:
                node_weight[i] = d
                parents[i] = (0,0)
            else:
                pass
            log("Node Weights: {}".format(node_weight))
            log(parents)
            """

if __name__ == "__main__":
    main()
