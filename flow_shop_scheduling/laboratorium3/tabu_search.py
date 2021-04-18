import math
from collections import deque
from typing import List

from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import *
from labolatorium2.algorithm import Algorithm
from laboratorium3 import stop_conditions
from laboratorium3.stop_conditions import StopConditions, IterCondition
from laboratorium3.neightbourhood_generator import NeightbourhoodGenerator, SwapAll
from laboratorium3.initial_solution_generator import InitialSolutionGenerator, CopyTasks


class TabuSearch(Algorithm):
    name = "Algorytm tabu search"
    tabu_list_max_length = 10

    def __init__(self,
                initial_solution_generator: InitialSolutionGenerator = CopyTasks(),
                neigthbourhood_generator: NeightbourhoodGenerator = SwapAll(),
                stop_condition: StopConditions = IterCondition(10)) -> None:
        super().__init__()
        self.intial_solution_generator = initial_solution_generator
        self.neigthbourhood_generator = neigthbourhood_generator
        self.stop_condition = stop_condition
        self.name = f"{TabuSearch.name} ({initial_solution_generator.name}, {neigthbourhood_generator.name})"

    def run(self, machines: List[Machine], tasks: List[Task]) -> List[Machine]:
        """ Tabu search - przeszukiwanie z zabronieniami

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

        # Generowanie rozwiązania początkowego
        initial_solution = self.intial_solution_generator.run(machines, tasks)

        for task in initial_solution:
            for machine in machines:
                machine.add_task(task)

        initial_Cmax = Gantt(machines).get_duration()

        for machine in machines:
            machine.clear_tasks()

        best_solution = initial_solution.copy()
        best_Cmax = initial_Cmax
        current_neighborhood_best_solution = initial_solution.copy()

        # Inicjalizacja warunku stopu
        self.stop_condition.start()

        # Lista tabu jako kolejka FIFO
        tabu_list = deque(maxlen=TabuSearch.tabu_list_max_length)

        while True:
            # Generowanie sąsiedztwa
            neighbors = self.neigthbourhood_generator.run(current_neighborhood_best_solution)
            current_neighborhood_best_Cmax = math.inf
            for current_solution in neighbors:
                for task in current_solution:
                    for machine in machines:
                        machine.add_task(task)
                current_Cmax = Gantt(machines).get_duration()
                if current_Cmax < current_neighborhood_best_Cmax and current_solution not in tabu_list:
                    current_neighborhood_best_Cmax = current_Cmax
                    current_neighborhood_best_solution = current_solution
                    tabu_list.append(current_solution)
                for machine in machines:
                    machine.clear_tasks()
            if current_neighborhood_best_Cmax < best_Cmax:
                best_Cmax = current_neighborhood_best_Cmax
                best_solution = current_neighborhood_best_solution

            if self.stop_condition.stop(current_Cmax):
                break

        print(best_solution, best_Cmax)

        for task in best_solution:
            for machine in machines:
                machine.add_task(task)
        return machines
