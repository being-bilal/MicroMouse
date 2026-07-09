import API
from helper_func import *
import numpy as np


def main():
    log("Running...")
    API.moveForward()
    API.moveForwardHalf()
    API.turnRight45()
    API.moveForwardHalf()


if __name__ == "__main__":
    main()
