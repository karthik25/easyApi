from openapis import Openapis
from tasks.task import Task


class List(Task):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "list"

    def run(self, args):
        Openapis.print_all_apis()
