import shlex


class Stringutils:
    def __init__(self):
        pass

    @staticmethod
    def args_to_dict(arguments):
        lexer = shlex.shlex(arguments, posix=True)
        lexer.whitespace_split = True
        lexer.whitespace = ','
        props = dict(pair.split('=', 1) for pair in lexer)
        return props
