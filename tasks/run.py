from tasks.exec import Exec


class Run(Exec):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "run"

    def run(self, args):
        if len(args) != 1 and len(args) != 2:
            print("usage: run <identifier> [<dictionary>]")
            return

        super(Run, self).run(args)
