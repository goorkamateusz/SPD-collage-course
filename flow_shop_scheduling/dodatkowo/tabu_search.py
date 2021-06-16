import math
from collections import deque
from typing import List

from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import *
from labolatorium2.algorithm import Algorithm
from laboratorium3 import neightbourhood_generator, stop_conditions
from laboratorium3.stop_conditions import StopConditions, IterCondition
from laboratorium3.initial_solution_generator import InitialSolutionGenerator, CopyTasks


class TabuSearchV2(Algorithm):
    name = "Algorytm tabu search V2"

    def __init__(self,
                tabu_list_max_length: int = 10,
                initial_solution_generator: InitialSolutionGenerator = CopyTasks(),
                neigthbourhood_generator: neightbourhood_generator = neightbourhood_generator.SwapAll(),
                stop_condition: StopConditions = IterCondition(10)) -> None:
        super().__init__()
        self.intial_solution_generator = initial_solution_generator
        self.neigthbourhood_generator = neigthbourhood_generator
        self.stop_condition = stop_condition
        self.tabu_list_max_length = tabu_list_max_length
        self.name = f"{TabuSearchV2.name} ({tabu_list_max_length}, {initial_solution_generator.name}, {neigthbourhood_generator.name}, {stop_condition})"

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
        tabu_list = deque(maxlen=self.tabu_list_max_length)

        while True:
            # Generowanie sąsiedztwa
            neighbors = self.neigthbourhood_generator.run(current_neighborhood_best_solution)
            current_neighborhood_best_Cmax = math.inf

            for current_solution in neighbors:
                for task in current_solution:
                    for machine in machines:
                        machine.add_task(task)

                current_Cmax = Gantt(machines).get_duration()

                if current_Cmax < current_neighborhood_best_Cmax and self.not_in_tabulist(tabu_list):
                    current_neighborhood_best_Cmax = current_Cmax
                    current_neighborhood_best_solution = current_solution
                    tabu_list.append((self.neigthbourhood_generator.first, self.neigthbourhood_generator.second))

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

    def not_in_tabulist(self, tabu_list) -> bool:
        if (self.neigthbourhood_generator.first, self.neigthbourhood_generator.second) in tabu_list:
            return False
        if (self.neigthbourhood_generator.second, self.neigthbourhood_generator.first) in tabu_list:
            return False
        return True
