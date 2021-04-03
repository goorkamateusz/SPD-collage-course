from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task


class WithoutModification:
    name = "basic"

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        return sorted_tasks.popleft()
