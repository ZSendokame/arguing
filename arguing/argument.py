import sys

argv = sys.argv
argumentDict = {}

def set(argument, argumentType=None):
    if not argumentType == None:
        argumentDict[argument] = argumentType

    else:
        argumentDict[argument] = str

def get(argument):
    if argument in argv and not argument == sys.argv[-1]:
        argumentValue = sys.argv[sys.argv.index(argument) + 1]

    else:
        argumentValue = None

    if argument in argumentDict:
        argumentValue = argumentDict[argument](argumentValue)

    return argumentValue

def check(argument):
    return argument in sys.argv