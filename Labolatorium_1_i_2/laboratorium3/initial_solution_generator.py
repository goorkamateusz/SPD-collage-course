from typing import List

from labolatorium1.general_lib import *

Solution = List[Task]


class InitialSolutionGenerator:
    def run(self, task_list: List[Task]) -> List[Task]:
        raise NotImplementedError()


class CopyTasks(InitialSolutionGenerator):
    def run(self, task_list: List[Task]) -> List[Task]:
        return task_list.copy()
