from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task


class FirstModification:
    name = "first"

    def choose(self, sorted_tasks, gantt: Gantt) -> Task:
        return sorted_tasks.popleft()


class SecondModification:
    name = "second"

    def choose(self, sorted_tasks, gantt: Gantt) -> Task:
        return sorted_tasks.popleft()


class ThirdModification:
    name = "third"

    def choose(self, sorted_tasks, gantt: Gantt) -> Task:
        return sorted_tasks.popleft()


class FourthModification:
    name = "fourth"
    
    def choose(self, sorted_tasks, gantt: Gantt) -> Task:
        return sorted_tasks.popleft()
