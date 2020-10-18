import shlex
from tasks.setter import Setter


class Set:
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "set"

    def run(self, args):
        type = args[0]
        values = args[1:]
        current_keys = Setter.get_current_keys()
        if type == "list":
            Setter.print_current_keys()
        if type == "multiple":
            lexer = shlex.shlex(values, posix=True)
            lexer.whitespace_split = True
            lexer.whitespace = ','
            props = dict(pair.split('=', 1) for pair in lexer)
            Setter.set_multiple_keys(props)
        if type in current_keys:
            print("Set: setting {0}".format(type))
            Setter.set_key_value(type, values[0])

