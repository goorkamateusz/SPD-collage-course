from typing import List

from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task
from laboratorium4.schrage_algorithm import SchrageAlgorithm


class CalierAlgorithm(Algorithm):
    name = 'Calier Algorithm'
    id = 5

    def count_task_b(self, tasks: List[Task]) -> Task:

        tempTask = Task(0,0,0,0)

        return tempTask

    #######################################################################

    def count_task_a(self, tasks: List[Task]) -> Task:

        tempTask = Task(0,0,0,0)

        return tempTask

    #######################################################################

    def count_task_c(self, tasks: List[Task]) -> Task:

        tempTask = Task(0,0,0,0)

        return tempTask
    
    #######################################################################

    def fill_list_k(self, tasks: List[Task]) -> Task:

        return []

    #######################################################################

    def run(self, tasks: List[Task]) -> List[Task]:
        
        upper_band = []
        partial_tasks_order = SchrageAlgorithm.run(tasks)

        if partial_tasks_order < upper_band:
            upper_band = partial_tasks_order
        
        task_b = self.count_task_b(tasks)
        task_a = self.count_task_a(tasks)
        task_c = self.count_task_c(tasks)

        # -1 w delivery time oznacza, że nie znaleziono zadania c
        if task_c.get_delivery_time() == -1:
            return partial_tasks_order

        list_k = self.fill_list_k(tasks)

        """
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
        """

        return partial_tasks_order
