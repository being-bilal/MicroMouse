import API 
from helper_func import log, maze_info, solver_info

def main():
    log("Running...")
    maze_info()
    API.setColor(0, 0, "R")
    API.setText(0, 0, "START")
    API.moveForward()
    API.turnLeft45()
if __name__ == "__main__":
    main()