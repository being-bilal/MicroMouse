import API 
from helper_func import *
import numpy 
from collections import deque

nodes = deque([0, 0])  
visited
def main():
    log("Running...")
    maze_info()
    API.setColor(0, 0, "R")
    API.setText(0, 0, "START")
    while True:
        API.setColor(0, 0, "R")
        if not API.wallLeft():
            nodes.append(get_position())
            turnLeft()
        while API.wallFront():
            nodes.append(get_position())
            turnRight()
        moveForward()
        log(get_position())
        log(nodes)
if __name__ == "__main__":
    main()