import sys

argv = sys.argv
argumentDict = {}

def set(argument, argumentType=str):
    argumentDict[argument] = argumentType

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