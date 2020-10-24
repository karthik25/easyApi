import shlex
from loader import Loader
from openapis import Openapis
from settings import Settings


class Shell:
    def __init__(self):
        pass

    def start(self):
        oapi_url = Settings.get_value_by_key("oapi_url")
        read_status = Openapis.populate_all_apis(oapi_url)

        if not read_status:
            print("easyApi Shell: failed to start")
            return

        loader = Loader()
        print("easyApi Shell: valid commands are (valid commands are 'set', 'list', 'exec', 'filter', 'clear', 'exit' or 'help')")
        print("easyApi Shell: use the command 'exec' to run an api, run 'help' for more details")
        print("easyApi Shell: 'exec' also has aliases like 'call', 'run'")
        print("easyApi Shell: use the command 'result' to see the last result")
        print("easyApi Shell: run the command 'set list' to view the current settings")
        print("easyApi Shell: run the command 'list' and press enter to view the apis")
        command = ""
        while command != "exit":
            command = input("> ")

            if command == "exit":
                return

            try:
                task_splits = shlex.split(command)
                task_identifier = task_splits[0]
                task_instance = loader.get_by_identifier(task_identifier)
                if task_instance is None:
                    print("easyApi Shell: Don't know how to handle this")
                else:
                    task_instance.run(task_splits[1:])
            except:
                print("easyApi Shell: something went wrong")
