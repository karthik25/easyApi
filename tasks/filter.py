import json
from result import Result


class Filter:
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "filter"

    def run(self, args):
        if len(args) != 2:
            print("usage: filter <field> <value>")
            return
        last_result = Result.last_result
        result_items = []
        for item in last_result:
            if item[args[0]] == args[1]:
                result_items.append(item)
        print(json.dumps(result_items, indent=4))

