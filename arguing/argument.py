import sys

argv = sys.argv
argument_dict = {}


def set(argument, type=str, default=None, mandatory=False, help=None):
    argument_dict[argument] = {
        'default': default,
        'type': type,
        'help': help
    }

    if mandatory and not check(argument):
        exit(f'{argument}: {help} ({type.__name__}).')

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
    return (argument in argv
            and argv.index(argument) + 1 < len(argv))
