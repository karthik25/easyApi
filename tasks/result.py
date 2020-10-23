import result
import json


class Result:
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