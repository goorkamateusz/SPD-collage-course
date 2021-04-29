from typing import List
import math

from laboratorium4.priority_queue import PriorityQueue
from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task


class SchragePMTNNLogNAlgorithm(Algorithm):
    name = 'Schrage PMTN nLog(n) Algorithm'

    def run(self, tasks: List[Task]) -> int:
        tasks_ready = PriorityQueue(key=Task.get_delivery_time)
        tasks_not_ready = PriorityQueue(tasks, key=Task.get_preparation_time, reverse=True)
        l = Task(-1, 0, 0, math.inf)
        t = tasks_not_ready.top().get_preparation_time()
        c_max = 0

        while tasks_ready or tasks_not_ready:
            while tasks_not_ready and tasks_not_ready.top().get_preparation_time() <= t:
                j_star = tasks_not_ready.extract()
                tasks_ready.insert(j_star)

                if j_star.get_delivery_time() > l.get_delivery_time():
                    l.set_execution_time(t - j_star.get_preparation_time())
                    t = j_star.get_preparation_time()

                    if l.get_execution_time() > 0:
                        tasks_ready.insert(l)

            if not tasks_ready:
                t = tasks_not_ready.top().get_preparation_time()
            else:
                j_star = tasks_ready.extract()
                l = j_star
                t += j_star.get_execution_time()
                c_max = max(c_max, t + j_star.get_delivery_time())

        return c_max
