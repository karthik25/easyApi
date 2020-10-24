import shlex
from settings import Settings


class Set:
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "set"

    def run(self, args):
        if len(args) == 0:
            print("usage: set <key> <value> or set list")
            return

        type = args[0]
        values = args[1] if len(args) > 1 else ""
        current_keys = Settings.get_current_keys()
        if type == "list":
            Settings.print_current_keys()
        if type == "multiple":
            lexer = shlex.shlex(values, posix=True)
            lexer.whitespace_split = True
            lexer.whitespace = ','
            props = dict(pair.split('=', 1) for pair in lexer)
            Settings.set_multiple_keys(props)
        if type in current_keys:
            print("Set: setting {0}".format(type))
            Settings.set_key_value(type, values)

