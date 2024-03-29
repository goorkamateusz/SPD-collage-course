from typing import List
import math

from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task


class SchragePMTNAlgorithm(Algorithm):
    name = 'Schrage PMTN Algorithm'
    id = 2

    def run(self, tasks: List[Task]) -> int:
        tasks_ready = set()
        tasks_not_ready = set(tasks)
        l = Task(-1, 0, 0, math.inf)
        t = min(task.get_preparation_time() for task in tasks_not_ready)
        c_max = 0

        while tasks_ready or tasks_not_ready:
            while tasks_not_ready and min(task.get_preparation_time() for task in tasks_not_ready) <= t:
                j_star = min(tasks_not_ready, key=Task.get_preparation_time)
                tasks_not_ready.remove(j_star)
                tasks_ready.add(j_star)

                if j_star.get_delivery_time() > l.get_delivery_time():
                    l = l.copy().change_execution_time(t - j_star.get_preparation_time())
                    t = j_star.get_preparation_time()

                    if l.get_execution_time() > 0:
                        tasks_ready.add(l)

            if not tasks_ready:
                t = min(task.get_preparation_time() for task in tasks_not_ready)
            else:
                j_star = max(tasks_ready, key=Task.get_delivery_time)
                tasks_ready.remove(j_star)
                l = j_star
                t += j_star.get_execution_time()
                c_max = max(c_max, t + j_star.get_delivery_time())

        return c_max
