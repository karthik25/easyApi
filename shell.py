import shlex
from loader import Loader
from openapis import Openapis
from tasks.setter import Setter


class Shell:
    def __init__(self):
        pass

    def start(self):
        oapi_url = Setter.get_value_by_key("oapi_url")
        Openapis.populate_all_apis(oapi_url)
        loader = Loader()
        print("Shell: enter your command ('set', 'list', 'exec', 'filter' or 'help')")
        print("Shell: exec also has aliases like 'call', 'run'")
        print("Shell: use the command 'result' to see the last result")
        print("Shell: use the command 'clear' to clear the screen")
        print("Shell: use the command 'exit' to exit easyApi")
        command = ""
        while command != "exit":
            command = input("> ")

            if command == "exit":
                return

            task_splits = shlex.split(command)
            task_identifier = task_splits[0]
            task_instance = loader.get_by_identifier(task_identifier)
            if task_instance is None:
                print("Shell: Don't know how to handle this")
            else:
                task_instance.run(task_splits[1:])
