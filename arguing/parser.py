import sys
from typing import Any


class Arguing:
    def __init__(self, help: str = '') -> None:
        self.help = help
        self.arguments = {}
        self.argv = sys.argv

    def set(self, name: str, flag: bool = False, type: type = str, default: Any = None, required: bool = False) -> Any:
        self.arguments[name] = {
            'is_flag': flag,
            'default': default,
            'type': type
        }

        if not flag and (required or (name not in self.argv)):
            exit(self.help)

        return self.get(name)

    def get(self, name: str) -> Any:
        position = -1 if name not in self.argv else self.argv.index(name)

        if self.arguments[name]['is_flag']:
            return bool(position)

        elif position != -1 and not self.next(position).startswith('-'):
            return self.arguments[name].get('type', str)(self.next(position))

        return self.arguments[name]['default']

    def next(self, pos: int = 0) -> str:
        return None if len(self.argv) < pos + 1 else self.argv[pos + 1]

    def pipe() -> str:
        if sys.stdin.isatty():
            return None

        return sys.stdin.readline().strip()
