import os


class Clear:
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "clear"

    def run(self, args):
        os.system("cls")
