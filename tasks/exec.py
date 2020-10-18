class Exec:
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "exec"

    def run(self, args):
        print("Hello from 'exec'")

