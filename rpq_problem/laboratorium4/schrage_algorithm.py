from typing import List

from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task


class SchrageAlgorithm(Algorithm):
    name = 'Schrage Algorithm'
    id = 0

    def run(self, tasks: List[Task]) -> List[Task]:
        partial_tasks_order = []
        tasks_ready_for_scheduling = set()
        tasks_not_ready_for_scheduling = set(tasks)
        t = min(task.get_preparation_time() for task in tasks_not_ready_for_scheduling)

        while tasks_ready_for_scheduling or tasks_not_ready_for_scheduling:
            while tasks_not_ready_for_scheduling and min(task.get_preparation_time() for task in tasks_not_ready_for_scheduling) <= t:
                j_star = min(tasks_not_ready_for_scheduling, key=Task.get_preparation_time)
                tasks_ready_for_scheduling.add(j_star)
                tasks_not_ready_for_scheduling.remove(j_star)

            if not tasks_ready_for_scheduling:
                t = min(task.get_preparation_time() for task in tasks_not_ready_for_scheduling)
            else:
                j_star = max(tasks_ready_for_scheduling, key=Task.get_delivery_time)
                tasks_ready_for_scheduling.remove(j_star)
                partial_tasks_order.append(j_star)
                t += j_star.get_execution_time()

        return partial_tasks_order
