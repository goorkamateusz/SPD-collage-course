from laboratorium4.Cmax_calculator import CMaxCalculator
from typing import List

from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task
from laboratorium4.schrage_algorithm import SchrageAlgorithm
from laboratorium4.schrage_pmtn import SchragePMTNAlgorithm


class CalierAlgorithm(Algorithm):
    name = 'Calier Algorithm'
    id = 5

    cmax_calc = CMaxCalculator()

    #######################################################################
    #TODO!!!

    def count_task_b(self, tasks: List[Task]) -> Task:

        tempTask = tasks[-1]
        cmax = self.cmax_calc.get_Cmax(tasks)

        for task in tasks:
            tmp_q = task.get_delivery_time()
            task.change_delivery_time(tmp_q+1)
            
            if cmax == self.cmax_calc.get_Cmax(tasks) + 1:
                tempTask = task
            task.change_delivery_time(tmp_q)

        return tempTask

    #######################################################################
    #TODO!!!

    def count_task_a(self, tasks: List[Task]) -> Task:

        tempTask = Task(0,0,0,0)

        return tempTask

    #######################################################################
    #TODO!!!

    def count_task_c(self, tasks: List[Task], task_a, task_b) -> Task:

        tempTask = Task(0,-1,0,0)

        sublist = tasks[tasks.index(task_a) + 1:tasks.index(task_b)]


        return tempTask

    #######################################################################
    #TODO!!!

    def count_h_K(self, tasks: List[Task]) -> int:

        return 0
    
    #######################################################################
    #TODO!!!

    def fill_list_k(self, tasks: List[Task], task_c, task_b) -> Task:

        return tasks[tasks.index(task_c) + 1:tasks.index(task_b) + 1]

    #######################################################################
    #TODO!!!

    def run(self, tasks: List[Task], upper_band = 9999) -> List[Task]:
        
        partial_tasks_order = List[Task]

        schrage = SchrageAlgorithm()
        schragePMTN = SchragePMTNAlgorithm()

        #################################

        temp_tasks_order = schrage.run(tasks)
        var_u = self.cmax_calc.get_Cmax(temp_tasks_order)

        if var_u < upper_band:
            upper_band = var_u
            partial_tasks_order = temp_tasks_order
        
        task_b = self.count_task_b(tasks)
        task_a = self.count_task_a(tasks)
        task_c = self.count_task_c(tasks, task_a, task_b)

        #################################

        # -1 w delivery time oznacza, że nie znaleziono zadania c
        if task_c.get_delivery_time() == -1:
            return partial_tasks_order

        list_K = self.fill_list_k(tasks, task_c, task_b)

        r_K = min(task.get_preparation_time() for task in tasks)
        q_K = min(task.get_delivery_time() for task in tasks)
        p_K = 0
        for task in list_K:
            p_K += task.get_execution_time()

        #################################

        task_c_copy = task_c.copy()
        task_c.change_preparation_time(max([task_c.get_preparation_time(), r_K + p_K]))
        
        lower_band = schragePMTN.run(tasks)
        lower_band = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K), lower_band)

        if lower_band < upper_band:
            self.run(tasks, upper_band)
        
        #################################

        task_c = task_c_copy.copy()

        task_c.change_delivery_time(max([task_c.get_delivery_time(), r_K + p_K]))

        lower_band = schragePMTN.run(tasks)
        lower_band = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K), lower_band)

        if lower_band < upper_band:
            self.run(tasks, upper_band)

        task_c = task_c_copy.copy()

        return partial_tasks_order
