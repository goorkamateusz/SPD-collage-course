from typing import List

from labolatorium1.general_lib import *
from labolatorium2.algorithm import Algorithm

Solution = List[Task]


class InitialSolutionGenerator:
    name = ""

    def run(self, machines: List[Machine], task_list: List[Task]) -> List[Task]:
        raise NotImplementedError()


class CopyTasks(InitialSolutionGenerator):
    name = "Copy tasks"

    def run(self, machines: List[Machine], task_list: List[Task]) -> List[Task]:
        return task_list.copy()


class UseAlgorithm(InitialSolutionGenerator):
    def __init__(self, alg: Algorithm):
        self.alg = alg
        self.name = str(alg)

    def run(self, machines: List[Machine], task_list: List[Task]) -> List[Task]:
        machines = self.alg.run(machines, task_list)
        first_machine = machines[0]
        return first_machine.tasks
