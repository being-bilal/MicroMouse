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

def turnLeft():
    global heading
    idx = directions.index(heading)
    heading = directions[(idx - 1) % 4]   
    API.turnLeft()

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
    API.moveForward()
