import result
import json
from tasks.task import Task


class Result(Task):
    def __init__(self):
        pass

    @staticmethod
    def handles():
        return "result"

    def run(self, args):
        if result.Result.result_type == "application/json":
            print(json.dumps(result.Result.last_result, indent=4))
        else:
            print(result.Result.last_result)