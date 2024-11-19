from command import Command


class God(Command):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"God of {self.name}"

    def lazyfriend(self, name):
        return f"Lazy friend of {self.name} is {name}"

    def auto(self, name):
        return f"Auto of {self.name} is {name}"

    def beagod(self, name):
        return f"Beagod of {self.name} is {name}"
