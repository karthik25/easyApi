from helptext import Helptext
from tasks.task import Task


class Help(Task):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "help"

    def run(self, args):
        Helptext.print_help_text()