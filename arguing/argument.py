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
        exit(documentation())

    return get(argument)


def get(argument):
    if argument in argv and argv.index(argument) < len(argv) - 1:
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


def documentation():
    documentation_message = f'{argv[0]} usage:\n\n'
    documentation_message += 'Parameters:\n'

    for argument in argument_dict:
        argument_type = argument_dict[argument]['type'].__name__
        argument_default = argument_dict[argument]['default']
        argument_help = argument_dict[argument]['help']

        documentation_message += f'\t{argument}: {argument_help} ' \
            f'(Type: {argument_type}, Default: {argument_default})\n'

    return documentation_message
