from typing import List

from laboratorium4.task import Task
from laboratorium4.algorithm import Algorithm

Solution = List[Task]


class InitialSolutionGenerator:
    name = ""

    def run(self, task_list: List[Task]) -> List[Task]:
        raise NotImplementedError()


class CopyTasks(InitialSolutionGenerator):
    name = "Copy tasks"

    def run(self, task_list: List[Task]) -> List[Task]:
        return task_list.copy()


class UseAlgorithm(InitialSolutionGenerator):
    def __init__(self, alg: Algorithm):
        self.alg = alg
        self.name = str(alg)

    def run(self, task_list: List[Task]) -> List[Task]:
        tasks = self.alg.run(task_list.copy())
        return tasks[0].tasks.copy()
