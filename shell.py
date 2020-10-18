import shlex
from loader import Loader
from openapis import Openapis


class Shell:
    def __init__(self):
        pass

    def start(self, oapi_url):
        Openapis.populate_all_apis(oapi_url)
        loader = Loader()
        print("Shell: Enter your command (set, list or exec)")
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
