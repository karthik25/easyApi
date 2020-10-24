import inspect
from tasks.task import Task
from tasks.set import Set
from tasks.list import List
from tasks.exec import Exec
from tasks.clear import Clear
from tasks.filter import Filter
from tasks.call import Call
from tasks.run import Run
from tasks.result import Result
from tasks.help import Help


class Loader:
    def __init__(self):
        pass

    def get_by_identifier(self, identifier):
        # create a dictionary and store it in Typedict (say)
        all_cls = globals()
        for cls in all_cls:
            current_cls = globals()[cls]
            if inspect.isclass(current_cls) and issubclass(current_cls, Task):
                handles = getattr(current_cls, "handles", None)
                if handles is not None:
                    handles_value = handles()
                    if handles_value == identifier:
                        return current_cls()
        return None
