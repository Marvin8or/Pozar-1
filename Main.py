from FunctionDefinitions import mainFunction, writeToFile
from PathController import *
import sys
import numpy as np

if __name__ == "__main__":
    _X = sys.argv[1]
    _Y = sys.argv[2]
    _T = sys.argv[3]
    X = [_X, _Y, _T]
    diff = mainFunction(X)