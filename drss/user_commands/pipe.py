from command import Command


class pipe(Command):
    def __init__(self, *args):
        self.commands = args

    def __ror__(self, other):
        for command in self.commands:
            other = command(other)
        return other
