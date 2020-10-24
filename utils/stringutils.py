import shlex
import json


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

    @staticmethod
    def config_file_to_dict(file_name):
        try:
            with open(file_name, 'r') as file:
                json_file_data = file.read()

            settings = json.loads(json_file_data)
            return settings
        except:
            print("easyApi Shell: configuration file passed cannot be parsed, so ignoring")
            return {}