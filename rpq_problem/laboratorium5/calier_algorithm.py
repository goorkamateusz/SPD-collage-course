from typing import List

from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task
from laboratorium4.schrage_algorithm import SchrageAlgorithm
from laboratorium4.schrage_pmtn import SchragePMTNAlgorithm


class CalierAlgorithm(Algorithm):
    name = 'Calier Algorithm'
    id = 5

    #######################################################################
    #TODO!!!

    def count_task_b(self, tasks: List[Task]) -> Task:

        tempTask = Task(0,0,0,0)

        return tempTask

    #######################################################################
    #TODO!!!

    def count_task_a(self, tasks: List[Task]) -> Task:

        tempTask = Task(0,0,0,0)

        return tempTask

    #######################################################################
    #TODO!!!

    def count_task_c(self, tasks: List[Task]) -> Task:

        tempTask = Task(0,-1,0,0)

        return tempTask

    #######################################################################
    #TODO!!!

    def count_h_K(self, tasks: List[Task]) -> int:

        return 0
    
    #######################################################################
    #TODO!!!

    def fill_list_k(self, tasks: List[Task]) -> Task:

        list_k = []

        return list_k

    #######################################################################
    #TODO!!!

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

        list_K = self.fill_list_k(tasks)

        r_K = min(task.get_preparation_time() for task in tasks)
        q_K = min(task.get_delivery_time() for task in tasks)
        p_K = 0
        for task in list_K:
            p_K += task.get_execution_time()

        task_c.change_preparation_time(max([task_c.get_preparation_time(), r_K + p_K]))
        
        lower_band = SchragePMTNAlgorithm.run(tasks)
        lower_band = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K, lower_band))

        if lower_band < upper_band:
            self.run(tasks)
        
        # odtworzenie r_pi_c...

        task_c.change_delivery_time(max([task_c.get_delivery_time(), r_K + p_K]))

        lower_band = SchragePMTNAlgorithm.run(tasks)
        lower_band = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K, lower_band))

        if lower_band < upper_band:
            self.run(tasks)

        # odtworzenie q_pi_c...

        return partial_tasks_order
