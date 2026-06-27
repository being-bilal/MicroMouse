import sys
import API

position = (0, 0)
heading = "N"
directions = ["N", "E", "S", "W"]   

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def maze_info():
    log("mazeWidth: {}".format(API.mazeWidth()))
    log("mazeHeight: {}".format(API.mazeHeight()))

def solver_info():
    log("wallFront: {}".format(API.wallFront()))
    log("wallBack: {}".format(API.wallBack()))
    log("wallLeft: {}".format(API.wallLeft()))
    log("wallRight: {}".format(API.wallRight()))

def get_position():
    return position

def get_heading():
    return heading

def turnLeft():
    global heading
    idx = directions.index(heading)
    heading = directions[(idx - 1) % 4]   
    API.turnLeft()
    
def node_sort_key(node):
    # Put (0,0) first, then sort by x and y
    return (0 if node == (0, 0) else 1, node[0], node[1])

def turnRight():
    global heading
    idx = directions.index(heading)
    heading = directions[(idx + 1) % 4] 
    API.turnRight()

def moveForward():
    global position
    if heading == "N":
        position = (position[0], position[1] + 1)
    elif heading == "E":
        position = (position[0] + 1, position[1])
    elif heading == "S":
        position = (position[0], position[1] - 1)
    elif heading == "W":
        position = (position[0] - 1, position[1])
    x, y = get_position()
    API.setColor(x, y, "G")
    API.moveForward()
