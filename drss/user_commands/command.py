import importlib
import os
import sys


class Command:
    name: str
    Command_list: list = ['lazyfirend', 'auto', 'begod', 'god']

    def __init__(self, name, description, usage, func):
        self.name = name
        self.description = description
        self.usage = usage

    # 判断是不是command
    @classmethod
    def is_command(cls, command: str) -> bool:
        return command in cls.Command_list

    def execute(self, args) -> str | None:

    def
