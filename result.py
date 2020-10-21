class Result:
    def __init__(self):
        pass

    last_result = None

    @staticmethod
    def store_result(obj):
        Result.last_result = obj
