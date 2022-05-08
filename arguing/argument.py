import sys

sys.argv = sys.argv[1:]
argumentDict = {}

def setArgument(argument, argumentType=None):
    if not argumentType == None:
        argumentDict[argument] = argumentType

    else:
        argumentDict[argument] = str

def getArgument(argument):
    if not argument == sys.argv[-1]:
        argumentValue = sys.argv[sys.argv.index(argument) + 1]

    else:
        argumentValue = None

    if argument in argumentDict:
        argumentValue = argumentDict[argument](argumentValue)

    return argumentValue

def checkArgument(argument):
    return argument in sys.argv