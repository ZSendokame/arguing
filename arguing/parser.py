import sys
from typing import Any

argv = sys.argv
argument_dict = {}


def set(argument: str, type: type = str, default: Any = None, mandatory: bool = False, help: str = None) -> Any:
    argument_dict[argument] = {
        'default': default,
        'type': type,
        'help': help,
        'mandatory': mandatory
    }

    if mandatory and not check(argument):
        exit(f'{argument}: {help} ({type.__name__}).')

    return get(argument)


def get(argument: str) -> Any:
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


def check(argument: str) -> Any:
    return (argument in argv
            and len(argv) > argv.index(argument) + 1)


def pipe() -> str:
    if sys.stdin.isatty():
        return None

    return sys.stdin.readline().strip()
