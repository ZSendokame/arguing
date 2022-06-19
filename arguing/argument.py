import sys

argv = sys.argv
argumentDict = {}

def set(argument, argumentType=str, default=None, helpMessage=None):
    argumentDict[argument] = {
        'default': default,
        'type': argumentType,
        'help': helpMessage
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

def documentation():
    documentationMessage = f'{argv[0]} usage:\n\n'
    documentationMessage += 'Parameters:\n'

    for argument in argumentDict:
        argumentType = argumentDict[argument]['type'].__name__
        argumentDefault = argumentDict[argument]['default']
        argumentHelp = argumentDict[argument]['help']

        documentationMessage += f'\t{argument}: {argumentHelp} ' \
            f'(Type: {argumentType}, Default: {argumentDefault})'

    return documentationMessage