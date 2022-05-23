import sys

argv = sys.argv
argumentDict = {}

def set(argument, argumentType=str, help=None):
    argumentDict[argument] = {
        'type': argumentType,
        'help': help
    }

    if not argument in argv:
        raise Exception(f'Mandatory argument "{argument}" cannot be founded.\n{argument}: {help}')

def get(argument):
    if argument in argv and not argument == argv[-1]:
        argumentValue = argv[argv.index(argument) + 1]

    else:
        argumentValue = None

    if argument in argumentDict:
        argumentValue = argumentDict[argument](argumentValue)

    return argumentValue

def check(argument):
    return argument in argv

def help():
    helpMessage = ''
    helpMessage += f'USAGE: python {argv[0]} -h\n'

    for argument in argumentDict:
        helpMessage += f'{argument}: {argumentDict[argument]["help"]}'

        if not argument == list(argumentDict)[-1]:
            helpMessage += '\n'

    return helpMessage