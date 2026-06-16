import sys
import API

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
