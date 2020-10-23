import pyclbr
import os
from tasks.set import Set
from tasks.list import List
from tasks.exec import Exec
from tasks.clear import Clear
from tasks.filter import Filter
from tasks.call import Call
from tasks.run import Run
from tasks.result import Result


class Loader:
    def __init__(self):
        pass

    def __has_class(self, class_name):
        all_cls = globals()
        for cls in all_cls:
            if cls == class_name:
                return True
        return False

    def __get_handles(self, class_name):
        has_cls = self.__has_class(class_name)
        if not has_cls:
            return ""

        task_class = globals()[class_name]
        handles = task_class.handles()
        return handles

    def __create_instance(self, class_name):
        task_class = globals()[class_name]
        task_instance = task_class()
        return task_instance

    def get_by_identifier(self, identifier):
        files = os.listdir("tasks")
        for file in files:
            file_name = os.path.splitext(file)[0]
            mod_name = "tasks.{0}".format(file_name)
            mod_info = pyclbr.readmodule(mod_name)
            for item in mod_info.values():
                if self.__get_handles(item.name) == identifier:
                    return self.__create_instance(item.name)
        return None

