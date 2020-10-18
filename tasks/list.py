from openapis import Openapis


class List:
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "list"

    def run(self, args):
        Openapis.print_all_apis()
