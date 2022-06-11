import sys

argv = sys.argv
argumentDict = {}

def set(argument, argumentType=str, default=None):
    argumentDict[argument] = {
        'default': default,
        'type': argumentType
    }

def get(argument):
    if argument in argv and argv.index(argument) < len(argv):
        valueIndex = argv.index(argument) + 1
        argumentValue = argv[valueIndex]

    elif argument in argumentDict:
        argumentValue = argumentDict[argument]['default']

    else:
        return None

    if argument in argumentDict:
        argumentValue = argumentDict[argument]['type'](argumentValue)

    return argumentValue

def check(argument):
    return argument in argv