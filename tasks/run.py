from tasks.exec import Exec


class Run(Exec):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "run"

    def run(self, args):
        super(Run, self).run(args)
