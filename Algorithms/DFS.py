import API 
from helper_func import *
import numpy 
from collections import deque

nodes = deque([0, 0])  
visited_nodes = set()
stack = []
target_node = (0,0)

def left_of(h):
    return directions[(directions.index(h) - 1) % 4]

def right_of(h):
    return directions[(directions.index(h) + 1) % 4]

def opposite(h):
    return directions[(directions.index(h) + 2) % 4]

def store_walls():
    x, y = get_position()
    heading = get_heading()
    if API.wallFront():
        API.setWall(x, y, heading.lower())
    if API.wallLeft():
        API.setWall(x, y, left_of(heading).lower())
    if API.wallRight():
        API.setWall(x, y, right_of(heading).lower())

def check_available_nodes():
    x, y = get_position()
    heading = get_heading()
    available_nodes = set()
    if heading == 'N':
        if not API.wallFront() and (x, y + 1) not in visited_nodes:
            available_nodes.add((x, y + 1))
        if not API.wallLeft() and (x - 1, y) not in visited_nodes:
            available_nodes.add((x - 1, y))
        if not API.wallRight() and (x + 1, y) not in visited_nodes:
            available_nodes.add((x + 1, y))
    elif heading == 'E':
        if not API.wallFront() and (x + 1, y) not in visited_nodes:
            available_nodes.add((x + 1, y))
        if not API.wallLeft() and (x, y + 1) not in visited_nodes:
            available_nodes.add((x, y + 1))
        if not API.wallRight() and (x, y - 1) not in visited_nodes:
            available_nodes.add((x, y - 1))
    elif heading == 'S':
        if not API.wallFront() and (x, y - 1) not in visited_nodes:
            available_nodes.add((x, y - 1))
        if not API.wallLeft() and (x + 1, y) not in visited_nodes:
            available_nodes.add((x + 1, y))
        if not API.wallRight() and (x - 1, y) not in visited_nodes:
            available_nodes.add((x - 1, y))
    elif heading == 'W':
        if not API.wallFront() and (x - 1, y) not in visited_nodes:
            available_nodes.add((x - 1, y))
        if not API.wallLeft() and (x, y - 1) not in visited_nodes:
            available_nodes.add((x, y - 1))
        if not API.wallRight() and (x, y + 1) not in visited_nodes:
            available_nodes.add((x, y + 1))
    return available_nodes

def move_to_target_node(target_node):
    x, y = get_position()
    target_x, target_y = target_node
    if target_x > x:
        while get_heading() != "E":
            turnRight()
        while get_position()[0] < target_x:
            moveForward()
    elif target_x < x:
        while get_heading() != "W":
            turnLeft()
        while get_position()[0] > target_x:
            moveForward()
    elif target_y > y:
        while get_heading() != "N":
            turnLeft()
        while get_position()[1] < target_y:
            moveForward()
    elif target_y < y:
        while get_heading() != "S":
            turnRight()
        while get_position()[1] > target_y:
            moveForward()

def main():
    log("Running...")
    maze_info()
    API.setColor(0, 0, "R")
    API.setText(0, 0, "START")
    while True:
        store_walls()
        stack.append(get_position())
        visited_nodes.add(get_position())
        available_nodes = check_available_nodes()
        log("Available nodes: {}".format(available_nodes))
        if available_nodes:
            target_node = available_nodes.pop()
        else:
            stack.pop()
            if not stack:
                log("NO MORE NODES TO VISIT, ENDING PROGRAM")
                break
            target_node = stack.pop()
            visited_nodes.add(target_node)
        
        move_to_target_node(target_node)
        log("Target node: {}".format(target_node))
        
        
if __name__ == "__main__":
    main()