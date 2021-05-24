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
    permutations = []

    #######################################################################
    def calier(self, tasks: List[Task], upper_band = 99999999) -> List[Task]:

        schrage = SchrageAlgorithm()
        schragePMTN = SchragePMTNAlgorithm()

        #################################

        temp_tasks_order = schrage.run(tasks)
        var_u = self.cmax_calc.get_Cmax(temp_tasks_order)

        if var_u < upper_band:
            upper_band = var_u
            tasks = temp_tasks_order
        
        task_b = self.count_task_b(tasks)
        task_a = self.count_task_a(tasks, task_b)
        task_c = self.count_task_c(tasks, task_a, task_b)

        #################################

        # -1 w delivery time oznacza, że nie znaleziono zadania c
        if task_c.get_preparation_time() == -1:
            return tasks

        list_K = self.fill_list_k(tasks, task_c, task_b)

        r_K = min(task.get_preparation_time() for task in list_K)
        q_K = min(task.get_delivery_time() for task in list_K)
        p_K = 0
        for task in list_K:
            p_K += task.get_execution_time()

        #################################

        task_c_copy = task_c.copy()
        task_c.change_preparation_time(max([task_c.get_preparation_time(), r_K + p_K]))
        
        lower_band = schragePMTN.run(tasks)
        lower_band = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K), lower_band)

        if lower_band < upper_band:
            self.calier(tasks, upper_band)
            #self.permutations.append([tasks, upper_band])
        
        #################################

        task_c = task_c_copy.copy()

        task_c.change_delivery_time(max([task_c.get_delivery_time(), r_K + p_K]))

        lower_band = schragePMTN.run(tasks)
        lower_band = max(self.count_h_K(list_K), self.count_h_K([task_c] + list_K), lower_band)

        if lower_band < upper_band:
            self.calier(tasks, upper_band)
            #self.permutations.append([tasks, upper_band])

        task_c = task_c_copy.copy()

        return tasks

    #######################################################################
    #TODO!!! test

    def count_task_b(self, tasks: List[Task]) -> Task:

        tempTask = tasks[-1]
        cmax = self.cmax_calc.get_Cmax(tasks)

        for task in tasks:
            tmp_q = task.get_delivery_time()
            task.change_delivery_time(tmp_q+10)
            
            if cmax == self.cmax_calc.get_Cmax(tasks) + 10:
                tempTask = task
            task.change_delivery_time(tmp_q)

        return tempTask

    #######################################################################
    #TODO!!! do

    def count_task_a(self, tasks: List[Task], task_b) -> Task:

        cmax = self.cmax_calc.get_Cmax(tasks)

        task_a = tasks[0]
        sum = task_a.get_preparation_time() + task_a.get_execution_time()

        for i in range(1, len(tasks)):

            if sum < tasks[i].get_preparation_time():

                task_a = tasks[i]

            sum += tasks[i].get_preparation_time() + tasks[i].get_execution_time()
            if tasks[i] == task_b:
                break

        return task_a


        """
        for task in tasks:
            tmp_r = task.get_preparation_time()
            task.change_preparation_time(tmp_r+10)
            
            if cmax == self.cmax_calc.get_Cmax(tasks) + 10:
                tempTask = task
                task.change_preparation_time(tmp_r)
                return tempTask
            else:
                task.change_preparation_time(tmp_r)
        """
        raise IndexError

    #######################################################################
    #TODO!!! test

    def count_task_c(self, tasks: List[Task], task_a: Task, task_b: Task) -> Task:

        tempTask = Task(0,-1,0,0)

        sublist = tasks[tasks.index(task_a) + 1:tasks.index(task_b)]

        for task in sublist:
            if task.get_delivery_time() < task_b.get_delivery_time():
                tempTask = task

        return tempTask

    #######################################################################
    #TODO!!! test

    def count_h_K(self, tasks: List[Task]) -> int:

        r_K = min(task.get_preparation_time() for task in tasks)
        q_K = min(task.get_delivery_time() for task in tasks)
        p_K = 0
        for task in tasks:
            p_K += task.get_execution_time()
        
        return r_K + p_K + q_K
    
    #######################################################################
    #TODO!!! test

    def fill_list_k(self, tasks: List[Task], task_c, task_b) -> Task:

        return tasks[tasks.index(task_c) + 1:tasks.index(task_b) + 1]

    #######################################################################
    #######################################################################
    #######################################################################
    #TODO!!! test

    def run(self, tasks: List[Task]) -> List[Task]:
        
        return self.calier(tasks, 99999)

        """
        self.permutations.append([tasks, 9999])

        temp_tasks = List[Task]
        best_tasks = List[Task]
        tmp_tsk = Task(1, 99999, 99999, 99999)
        best_tasks.append(tmp_tsk)

        i = 0
        while len(self.permutations) > 0:
            [a, b] = self.permutations.pop(0)
            temp_tasks = self.calier(a, b)
            if self.cmax_calc.get_Cmax(temp_tasks) < self.cmax_calc.get_Cmax(best_tasks):
                pass
                best_tasks = temp_tasks.copy()
            i += 1

        print("PERM: " + str(i))

        return best_tasks
        """