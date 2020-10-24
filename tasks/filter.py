import json
from result import Result
from utils.stringutils import Stringutils
from settings import Settings
from tasks.task import Task


class Filter(Task):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "filter"

    def run(self, args):
        if len(args) < 2:
            print("usage: filter <field> <value> [<option-dictionary>]")
            return
        filter_props = self.get_filter_props(args)
        last_result = Result.last_result
        result_items = []
        if Settings.is_debug():
            print("Filter: partial match mode {0}".format(filter_props["partial_match"]))
        for item in last_result:
            if filter_props["partial_match"]:
                if item[args[0]].find(args[1]) >= 0:
                    result_items.append(item)
            else:
                if item[args[0]] == args[1]:
                    result_items.append(item)
        print(json.dumps(result_items, indent=4))


    def get_filter_props(self, args):
        filter_props = {
            "partial_match": False
        }
        if len(args) != 3:
            return filter_props
        filter_dict = Stringutils.args_to_dict(args[2])
        if "partial_match" in filter_dict.keys():
            filter_props["partial_match"] = True if filter_dict["partial_match"] in ["true", "True", "1"] else False
        return filter_props
