from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task
from labolatorium2.critial_path import CritialPath


class FirstModification:
    name = "first"

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        cricial_path = gantt.get_critical_path()
        longest_task = max(cricial_path, key = lambda t: t.duration)

        if longest_task == optimal_task_list[-1]:
            cricial_path.remove(longest_task)
            longest_task = max(cricial_path, key = lambda t: t.duration)

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
