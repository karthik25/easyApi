from helptext import Helptext


class Help:
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "help"

    def run(self, args):
        Helptext.print_help_text()