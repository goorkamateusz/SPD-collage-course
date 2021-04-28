from typing import List
import math

from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task


class SchragePMTNAlgorithm(Algorithm):
    name = 'Schrage PMTN Algorithm'

    def run(self, tasks: List[Task]) -> List[Task]:
        partial_tasks_order = []
        tasks_ready = set()
        tasks_not_ready = set(tasks)
        l = Task(-1, 0, 0, math.inf)
        t = min(task.get_preparation_time() for task in tasks_not_ready)

        while tasks_ready or tasks_not_ready:
            while tasks_not_ready and min(task.get_preparation_time() for task in tasks_not_ready) <= t:
                j_star = min(tasks_not_ready, key=Task.get_preparation_time)
                tasks_ready.add(j_star)
                tasks_not_ready.remove(j_star)

                if j_star.get_delivery_time() > l.get_delivery_time():
                    l.set_execution_time(t - j_star.get_preparation_time())
                    t = j_star.get_preparation_time()

                    if l.get_execution_time() > 0:
                        tasks_ready.add(j_star) # w pseudo kodzie jest l*?

            if not tasks_ready:
                t = min(task.get_preparation_time() for task in tasks_not_ready)
            else:
                j_star = max(tasks_ready, key=Task.get_delivery_time)
                tasks_ready.remove(j_star)
                partial_tasks_order.append(j_star)
                t += j_star.get_execution_time()
                l = j_star

        return partial_tasks_order
