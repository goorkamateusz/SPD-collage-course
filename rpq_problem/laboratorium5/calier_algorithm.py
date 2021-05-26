from laboratorium4.Cmax_calculator import CMaxCalculator
from typing import List, Optional
import sys

from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task
from laboratorium4.schrage_algorithm import SchrageAlgorithm
from laboratorium4.schrage_pmtn import SchragePMTNAlgorithm

import copy


class CarlierAlgorithm(Algorithm):
    name = 'Carlier Algorithm'
    id = 5

    cmax_calc = CMaxCalculator()
    schrage = SchrageAlgorithm()
    schragePMTN = SchragePMTNAlgorithm()

    permutations = []
    recurency_nb = 0
    out_string = ""

    #######################################################################
    def carlier(self, tasks: List[Task], upper_bound: int = 99999999) -> List[Task]:
        
        self.recurency_nb += 1
        self.out_string += (", Iteracja: " + str(self.recurency_nb))
        #################################

        temp_tasks_order = self.schrage.run(tasks)
        var_u = self.cmax_calc.get_Cmax(temp_tasks_order)

        if var_u < upper_bound:
            upper_bound = var_u
            tasks = temp_tasks_order
        
        task_b = self.count_task_b(tasks)
        task_a = self.count_task_a(tasks, task_b)
        task_c = self.count_task_c(tasks, task_a, task_b)

        #################################

        # Nie znaleziono zadania c
        if task_c is None:
            return tasks

        list_K = self.fill_list_k(tasks, task_c, task_b)

        r_K = min(task.get_preparation_time() for task in list_K)
        q_K = min(task.get_delivery_time() for task in list_K)
        p_K = sum(task.get_execution_time() for task in list_K)

        #################################
        
        r_c_old = task_c.get_preparation_time()
        
        if r_K + p_K > r_c_old:
            task_c.change_preparation_time(r_K + p_K)

            lower_bound = self.schragePMTN.run(tasks)
            lower_bound = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K), lower_bound)

            if lower_bound < upper_bound:
                self.permutations.append([copy.deepcopy(tasks), upper_bound])
        
            task_c.change_preparation_time(r_c_old)

        #################################

        q_c_old = task_c.get_delivery_time()

        if q_K + p_K > q_c_old:
            task_c.change_delivery_time(q_K + p_K)

            lower_bound = self.schragePMTN.run(tasks)
            lower_bound = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K), lower_bound)
        
            if lower_bound < upper_bound:
                self.permutations.append([copy.deepcopy(tasks), upper_bound])

            task_c.change_delivery_time(q_c_old)

        return tasks

    #######################################################################
    #TODO!!! test

    def count_task_b(self, tasks: List[Task]) -> Task:
        offset = 10

        temp_task = None
        cmax = self.cmax_calc.get_Cmax(tasks)

        for task in tasks:
            tmp_q = task.get_delivery_time()
            task.change_delivery_time(tmp_q+offset)
            
            if cmax + offset == self.cmax_calc.get_Cmax(tasks):
                temp_task = task
            task.change_delivery_time(tmp_q)

        if temp_task == None:
            raise ValueError
        return temp_task

    #######################################################################
    #TODO!!! do

    def count_task_a(self, tasks: List[Task], task_b: Task) -> Task:
       
        task_a = tasks[0]
        sum = task_a.get_preparation_time() + task_a.get_execution_time()

        for i in range(1, len(tasks)):
            if sum < tasks[i].get_preparation_time():
                task_a = tasks[i]

            sum += tasks[i].get_preparation_time() + tasks[i].get_execution_time()
            if tasks[i] == task_b:
                break

        return task_a

    #######################################################################
    #TODO!!! test

    def count_task_c(self, tasks: List[Task], task_a: Task, task_b: Task) -> Optional[Task]:
        sublist = tasks[tasks.index(task_a):tasks.index(task_b) +1]
        temp_task = None

        for task in sublist:
            if task.get_delivery_time() < task_b.get_delivery_time():
                temp_task = task

        return temp_task

    #######################################################################
    #TODO!!! test

    def count_h_K(self, tasks: List[Task]) -> int:
        r_K = min(task.get_preparation_time() for task in tasks)
        q_K = min(task.get_delivery_time() for task in tasks)
        p_K = sum(task.get_execution_time() for task in tasks)

        return r_K + p_K + q_K
    
    #######################################################################
    #TODO!!! test

    def fill_list_k(self, tasks: List[Task], task_c: Task, task_b: Task) -> List[Task]:
        return tasks[tasks.index(task_c) + 1:tasks.index(task_b) + 1]

    #######################################################################
    #######################################################################
    #######################################################################
    #TODO!!! test

    def run(self, tasks: List[Task]) -> List[Task]:
        #sys.setrecursionlimit(99999)
        #return self.carlier(tasks)

        temp_tasks = self.carlier(tasks)
        best_tasks = temp_tasks.copy()

        temp_c_max = 9999999
        best_c_max = 9999999


        while len(self.permutations) > 0:

            [a, b] = self.permutations.pop()

            self.out_string = "Zostało: " + str(len(self.permutations))

            temp_tasks = self.carlier(a, b)
            temp_c_max = self.cmax_calc.get_Cmax(temp_tasks)
            
            self.out_string += ", Cmax: " + str(best_c_max)
            print(self.out_string)

            if temp_c_max < best_c_max:
                best_tasks = temp_tasks.copy()
                best_c_max = self.cmax_calc.get_Cmax(best_tasks)

        return best_tasks