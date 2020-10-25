from openapis import Openapis
from tasks.task import Task


class List(Task):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "list"

    def run(self, args):
        if len(args) == 0:
            Openapis.print_all_apis()
            return

        all_apis = Openapis.get_all_apis()
        filter_arg = args[0]
        filtered_apis = []
        if filter_arg.isnumeric():
            max_items = int(filter_arg)
            if max_items > 0:
                for i in range(max_items):
                    filtered_apis.append(all_apis[i])
        else:
            for api in all_apis:
                if api["url"].find(filter_arg) >= 0:
                    filtered_apis.append(api)

        Openapis.print_selected_apis(filtered_apis)

