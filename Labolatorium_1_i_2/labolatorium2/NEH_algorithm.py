import math
from collections import deque

from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import *
from typing import List


class NehAlgorithm:
    name = "Algorytm NEH"

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

        while sorted_tasks:
            smallest_Cmax = math.inf
            # Wyciąganie zadania o największej sumie czasów
            current_task = sorted_tasks.popleft()
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
                for machine in machines:
                    machine.clear_tasks()
            optimal_task_list = current_optimal_task_list

        print(smallest_Cmax)
        print(optimal_task_list)
        for task in optimal_task_list:
            for machine in machines:
                machine.add_task(task)
        return machines
