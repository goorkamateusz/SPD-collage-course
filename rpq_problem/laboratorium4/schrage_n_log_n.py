from typing import List

from laboratorium4.priority_queue import PriorityQueue
from laboratorium4.task import Task
from laboratorium4.algorithm import Algorithm


class SchrageNLogNAlgorithm(Algorithm):
    name = 'Schrage n log n Algorithm'
    id = 1

    def run(self, tasks: List[Task]) -> List[Task]:
        partial_tasks_order = []
        tasks_ready_for_scheduling = PriorityQueue(key=Task.get_delivery_time)
        tasks_not_ready_for_scheduling = PriorityQueue(tasks, key=Task.get_preparation_time, reverse=True)
        t = tasks_not_ready_for_scheduling.top().get_preparation_time()

        while tasks_ready_for_scheduling or tasks_not_ready_for_scheduling:
            while tasks_not_ready_for_scheduling and tasks_not_ready_for_scheduling.top().get_preparation_time() <= t:
                j_star = tasks_not_ready_for_scheduling.pop()
                tasks_ready_for_scheduling.append(j_star)

            if not tasks_ready_for_scheduling:
                t = tasks_not_ready_for_scheduling.top().get_preparation_time()
            else:
                j_star = tasks_ready_for_scheduling.pop()
                partial_tasks_order.append(j_star)
                t += j_star.get_execution_time()

        return partial_tasks_order
