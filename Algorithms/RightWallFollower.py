import API 
from helper_func import log, maze_info, solver_info

def main():
    log("Running...")
    maze_info()
    API.setColor(0, 0, "R")
    API.setText(0, 0, "START")
    while True:
        API.setColor(0, 0, "R")
        if not API.wallRight():
            API.turnRight()
        while API.wallFront():
            API.turnLeft()
        API.moveForward()
        solver_info()
        
if __name__ == "__main__":
    main()