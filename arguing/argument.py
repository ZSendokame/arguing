import sys

argv = sys.argv
argumentDict = {}

def set(argument, argumentType=str, default=None):
    argumentDict[argument] = {
        'default': default,
        'type': argumentType
    }

    if default == None and not argument in argv:
        raise Exception(f'{argument} cannot be founded.')

def get(argument):
    if argument in argv and not argument == sys.argv[-1]:
        argumentValue = sys.argv[sys.argv.index(argument) + 1]

    elif argument in argumentDict:
            argumentValue = argumentDict[argument]['default']

    else:
        return None

    if argument in argumentDict:
        argumentValue = argumentDict[argument]['type'](argumentValue)

    return argumentValue

def check(argument):
    return argument in sys.argv