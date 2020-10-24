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
    task_dictionary = {

    }

    def __init__(self):
        pass

    @staticmethod
    def get_by_identifier(identifier):
        Loader.populate_task_dictionary()
        if identifier in Loader.task_dictionary.keys():
            type = Loader.task_dictionary[identifier]
            return type()
        return None

    @staticmethod
    def populate_task_dictionary():
        if len(Loader.task_dictionary.keys()) == 0:
            all_cls = globals()
            for cls in all_cls:
                current_cls = globals()[cls]
                if inspect.isclass(current_cls) and issubclass(current_cls, Task):
                    handles = getattr(current_cls, "handles", None)
                    if handles is not None:
                        handles_value = handles()
                        Loader.task_dictionary[handles_value] = current_cls
