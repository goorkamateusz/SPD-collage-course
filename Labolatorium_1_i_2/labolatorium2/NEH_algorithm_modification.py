import math
from collections import deque
from typing import List

from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import *
from labolatorium2.algorithm import Algorithm


class NehAlgorithmModification(Algorithm):
    name = "Algorytm NEH"

    def __init__(self, choose_rule):
        self.choose_rule = choose_rule
        self.name = f"{NehAlgorithmModification.name} ({choose_rule.name})"

    def run(self, machines: List[Machine], tasks: List[Task]) -> List[Machine]:
        """ Algorytm NEH

        Parameters
        ----------
        machines : list
            Lista maszyn z ustawionymi czasami zadań;
        tasks : list
            Lista zadań;

        Returns
        -------
        list
            Lista maszyn z dodanymi zadaniami do listy;
        """

        # Priorytety dla każdego zadania, które są sumą wszystkich operacji danego zadania
        priorities = {}
        for task in tasks:
            priorities[task] = sum(machine.get_task_duration(task) for machine in machines)
        sorted_tasks = deque(sorted(priorities, key=priorities.get, reverse=True))
        optimal_task_list = []

        even_odd_switch = False

        while sorted_tasks:
            even_odd_switch = not even_odd_switch
            smallest_Cmax = math.inf

            if even_odd_switch:
                current_task = sorted_tasks.popleft()
            else:
                current_task = self.choose_rule.choose(sorted_tasks, optimal_task_list, optimal_gantt)
                if current_task == None:
                    continue

            for i in range(0, len(optimal_task_list) + 1):
                task_list_copy = optimal_task_list.copy()
                task_list_copy.insert(i, current_task)
                for task in task_list_copy:
                    for machine in machines:
                        machine.add_task(task)
                gantt = Gantt(machines)
                current_Cmax = gantt.get_duration()
                if current_Cmax < smallest_Cmax:
                    smallest_Cmax = current_Cmax
                    current_optimal_task_list = task_list_copy
                    optimal_gantt = gantt
                for machine in machines:
                    machine.clear_tasks()
            optimal_task_list = current_optimal_task_list

        print(smallest_Cmax)
        print(optimal_task_list)
        for task in optimal_task_list:
            for machine in machines:
                machine.add_task(task)
        return machines
