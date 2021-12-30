from FunctionDefinitions import mainFunction
import sys

if __name__ == "__main__":
    _X = sys.argv[1]
    _Y = sys.argv[2]
    _T = sys.argv[3]
    X = [_X, _Y, _T]
    mainFunction(X)