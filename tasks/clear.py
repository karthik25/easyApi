import os
from tasks.task import Task


class Clear(Task):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "clear"

    def run(self, args):
        os.system("cls")
