import math
from itertools import permutations
from typing import List

from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import *
from typing import List


class AllPossibilities:
    name = "Najlepsza z permutacji"

    def run(self, machines: List[Machine], tasks: List[Task]) -> List[Machine]:
        """ Sprawdza wszystkie możliwości

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

        task_permutations = permutations(tasks)
        shortest_time = math.inf
        best_permutation = tasks

        for task_permutation in task_permutations:
            for machine in machines:
                for task in task_permutation:
                    machine.add_task(task)
            gantt = Gantt(machines)
            # print(f"permutacja {task_permutation} Cmax = {gantt.get_duration()}")
            if gantt.get_duration() < shortest_time:
                shortest_time = gantt.get_duration()
                best_permutation = task_permutation
            for machine in machines:
                machine.clear_tasks()

        print(f"permutacja optymalna {best_permutation} Cmax = {shortest_time}")
        for machine in machines:
            for task in best_permutation:
                machine.add_task(task)

        return machines
