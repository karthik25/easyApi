import shlex
from loader import Loader
from openapis import Openapis
from tasks.setter import Setter


class Shell:
    def __init__(self):
        pass

    def start(self):
        oapi_url = Setter.get_value_by_key("oapi_url")
        read_status = Openapis.populate_all_apis(oapi_url)

        if not read_status:
            print("Shell: failed to start")
            return

        loader = Loader()
        print("Shell: enter your command ('set', 'list', 'exec', 'filter', 'clear', 'exit' or 'help')")
        print("Shell: exec also has aliases like 'call', 'run'")
        print("Shell: use the command 'result' to see the last result")
        command = ""
        while command != "exit":
            command = input("> ")

            if command == "exit":
                return

            # todo: add try...except
            task_splits = shlex.split(command)
            task_identifier = task_splits[0]
            task_instance = loader.get_by_identifier(task_identifier)
            if task_instance is None:
                print("Shell: Don't know how to handle this")
            else:
                task_instance.run(task_splits[1:])
