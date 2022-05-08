import sys

sys.argv = sys.argv[1:]
argumentDict = {}

def setArgument(argument, argumentType=None):
    if not argumentType == None:
        argumentDict[argument] = argumentType

    else:
        argumentDict[argument] = str()

def getArgument(argument):
    argumentValue = sys.argv[sys.argv.index(argument) + 1]
    argumentValue = argumentDict[argument](argumentValue)

    return argumentValue

def checkArgument(argument):
    return argument in sys.argv