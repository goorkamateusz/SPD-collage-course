from collections import deque
from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task


class FirstModification:
    name = "first"

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        longest_task = max(gantt.get_critical_path(), key = lambda t: t.duration)
        optimal_task_list.remove(longest_task)
        return longest_task


class SecondModification:
    name = "second"

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        # todo
        return sorted_tasks.popleft()


class ThirdModification:
    name = "third"

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        # todo
        return sorted_tasks.popleft()


class FourthModification:
    name = "fourth"

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        # todo
        return sorted_tasks.popleft()
