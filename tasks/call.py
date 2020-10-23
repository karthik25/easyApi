from tasks.exec import Exec


class Call(Exec):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "call"

    def run(self, args):
        super(Call, self).run(args)
