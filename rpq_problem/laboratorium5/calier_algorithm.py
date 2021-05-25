import copy
from laboratorium4.Cmax_calculator import CMaxCalculator
from typing import List, Optional
import sys

from laboratorium4.algorithm import Algorithm
from laboratorium4.task import Task
from laboratorium4.schrage_algorithm import SchrageAlgorithm
from laboratorium4.schrage_pmtn import SchragePMTNAlgorithm


class CarlierAlgorithm(Algorithm):
    name = 'Carlier Algorithm'
    id = 5

    cmax_calc = CMaxCalculator()
    schrage = SchrageAlgorithm()
    schragePMTN = SchragePMTNAlgorithm()

    permutations = []
    recurency_nb = 0

    #######################################################################
    def carlier(self, tasks: List[Task], upper_bound: int = 99999999) -> List[Task]:
        
        self.recurency_nb += 1
        print(self.recurency_nb)
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
        
        task_c_copy = task_c.copy()
        task_c.change_preparation_time(max(task_c.get_preparation_time(), r_K + p_K))
        # tasks[tasks.index(task_c)] = task_c

        lower_bound = self.schragePMTN.run(tasks)
        lower_bound = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K), lower_bound)

        if lower_bound < upper_bound:
            #tasks = self.carlier(tasks, upper_bound)
            self.permutations.append([tasks, upper_bound])
            return tasks

        #################################

        task_c.change_preparation_time(task_c_copy.get_preparation_time())

        task_c.change_delivery_time(max(task_c.get_delivery_time(), q_K + p_K))
        # tasks[tasks.index(task_c)] = task_c

        lower_bound = self.schragePMTN.run(tasks)
        lower_bound = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K), lower_bound)

        if lower_bound < upper_bound:
            #tasks = self.carlier(tasks, upper_bound)
            self.permutations.append([copy.deepcopy(tasks), upper_bound])
            return tasks

        # task_c = task_c_copy.copy()
        task_c.change_delivery_time(task_c_copy.get_delivery_time())
        # tasks[tasks.index(task_c)] = task_c

        return tasks

    #######################################################################
    #TODO!!! test

    def count_task_b(self, tasks: List[Task]) -> Task:
        cmax = self.cmax_calc.get_Cmax(tasks)

        for task in tasks:
            id = tasks.index(task)
            c = self.cmax_calc.get_Cmax(tasks[0 : id+1])
            if c == cmax:
                return task

        raise NotImplementedError()

    #######################################################################
    #TODO!!! do

    def count_task_a(self, tasks: List[Task], task_b: Task) -> Task:
        timeline = dict()
        t = 0

        for task in tasks:
            t = max(t, task.get_preparation_time())
            t += task.get_execution_time()
            timeline[task] = t

        last_correct = task_b

        for task in reversed(tasks[0 : tasks.index(task_b)]):
            if timeline[task] != timeline[last_correct] - last_correct.get_execution_time():
                break
            last_correct = task

        return last_correct

    #######################################################################
    #TODO!!! test

    def count_task_c(self, tasks: List[Task], task_a: Task, task_b: Task) -> Optional[Task]:
        for task in reversed(tasks[tasks.index(task_a) : tasks.index(task_b) + 1]):
            if task.get_delivery_time() < task_b.get_delivery_time():
                return task
        return None

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
        return tasks[tasks.index(task_c) + 1 : tasks.index(task_b) + 1]

    #######################################################################
    #######################################################################
    #######################################################################
    #TODO!!! test

    def run(self, tasks: List[Task]) -> List[Task]:
        # sys.setrecursionlimit(99999)
        # return self.carlier(tasks)

        temp_tasks = self.carlier(tasks)
        best_tasks = temp_tasks.copy()

        i = 0
        while len(self.permutations) > 0:
            [a, b] = self.permutations.pop(0)
            temp_tasks = self.carlier(a, b)
            if self.cmax_calc.get_Cmax(temp_tasks) < self.cmax_calc.get_Cmax(best_tasks):
                best_tasks = temp_tasks.copy()
            i += 1

        print(i)
        return best_tasks