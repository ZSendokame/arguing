import sys

argv = sys.argv
argument_dict = {}


def set(argument, argument_type=str, default=None, help_message=None,
        mandatory=False):

    argument_dict[argument] = {
        'default': default,
        'type': argument_type,
        'help': help_message
    }

    if mandatory and not check(argument):
        exit(f'- Cannot find "{argument}".')

    return get(argument)


def get(argument):
    if argument in argv and argument != argv[-1]:
        value_index = argv.index(argument) + 1
        argument_value = argv[value_index]

    elif argument in argument_dict:
        argument_value = argument_dict[argument]['default']

    else:
        return None

    if argument in argument_dict:
        argument_value = argument_dict[argument]['type'](argument_value)

    return argument_value


def check(argument):
    return argument in argv
