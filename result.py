class Result:
    def __init__(self):
        pass

    last_result = None
    result_type = ''

    @staticmethod
    def store_result(obj, type):
        Result.last_result = obj
        Result.result_type = type