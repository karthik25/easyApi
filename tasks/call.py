from tasks.exec import Exec


class Call(Exec):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "call"

    def run(self, args):
        if len(args) != 1 and len(args) != 2:
            print("usage: call <identifier> [<dictionary>]")
            return

        super(Call, self).run(args)
