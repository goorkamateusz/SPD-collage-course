"""
    Źródło
    (1) http://dominik.zelazny.staff.iiar.pwr.wroc.pl/materialy/Algorytm_NEH_(Metoda_wstawien_w_klasycznych_problemach_szeregowania._Cz._I._Problem_przeplywowy).pdf
"""

from labolatorium1.calculable_lib import TaskAssigned
from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task
from labolatorium2.critial_path import CritialPath

import math


class FirstModification:
    """ Znajduje najdłuższe zadanie na ścieżce krytycznej

        "Na ścieŜce krytycznej w grafie G(π ) znajdź operację o największym czasie
        wykonywania (wyłączając operacje zadania j). Jako zadanie x przyjmij zadanie, w którego
        skład wchodzi ta operacja." (1)
    """
    name = "pierwsza modyf."

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        cricial_path = gantt.get_critical_path()
        longest_task = max(cricial_path, key = lambda t: t.duration)

        if longest_task == optimal_task_list[-1]:
            cricial_path.remove(longest_task)
            longest_task = max(cricial_path, key = lambda t: t.duration)

        optimal_task_list.remove(longest_task)
        return longest_task


class SecondModification:
    """ Znajduje zadanie o największym obciążeniu na ścieżce krytycznej (zajmujące najwięcej czasu na ścieżce krytycznej)

        "Dla każdego zadania z permutacji π (z wyjątkiem zadania j) wyznacz
        obciążenie tego zadania ścieżką krytyczną definiowane jako suma czasów wykonywania
        tych jego operacji, które wchodzą w skład ścieŜki krytycznej w grafie G(π ) . Jako zadanie
        x przyjmij zadanie o największym obciąŜeniu." (1)
    """
    name = "druga modyf."

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        critial_path = gantt.get_critical_path()
        weight = {}
        for task in critial_path:
            if task in weight:
                weight[task] += task.duration
            else:
                if task != optimal_task_list[-1]:
                    weight[task] = task.duration
        if weight:
            chossen_task = max(weight, key=weight.get)
            optimal_task_list.remove(chossen_task)
            return chossen_task
        else:
            return None


class ThirdModification:
    """ Wymiera zadanie które najczęściej pojawia się na ścieżce krytycznej.

        "Wśród zadań z permutacji π (z wyjątkiem zadania j) znajdź zadanie o
        największej liczbie operacji wchodzących w skład ścieŜki krytycznej w grafie G(π ) . JeŜeli
        wybór jest jednoznaczny, przyjmij to zadanie jako x. W przeciwnym wypadku jako zadanie
        x przyjmij zadanie, które jednocześnie ma największą wartość priorytetu (1)." (1)
    """
    name = "trzecia modyf."

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        critial_path = gantt.get_critical_path()
        tasks_on_path = {}
        for task in critial_path:
            if task in tasks_on_path:
                tasks_on_path[task] += 1
            else:
                if task != optimal_task_list[-1]:
                    tasks_on_path[task] = 1
        if tasks_on_path:
            chossen_task = max(tasks_on_path, key=tasks_on_path.get)
            optimal_task_list.remove(chossen_task)
            return chossen_task
        return None


class FourthModification:
    """ Wybiera zadanie, którego usunięcie powoduje najwięszke zmnieszenie Cmax.

        " Jako zadanie x przyjmij to zadanie z permutacji π (z wyjątkiem zadania j),
        którego usuniecie z tej permutacji spowoduje największe zmniejszenie wartości funkcji
        celu. " (1)
    """
    name = "czwarta modyf."

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        machine_without_tasks = [machine.copy_without_task_queue() for machine in gantt.machines]
        min_Cmax = math.inf
        chossen_task = None

        for task_to_remove in optimal_task_list:
            task_list_copy = optimal_task_list.copy()
            task_list_copy.remove(task_to_remove)
            machines_copy = machine_without_tasks.copy()

            for task in task_list_copy:
                for machine in machines_copy:
                    machine.add_task(task)

            gantt = Gantt(machines_copy)
            if gantt.get_duration() < min_Cmax:
                min_Cmax = gantt.get_duration()
                chossen_task = task_to_remove

        if chossen_task:
            optimal_task_list.remove(chossen_task)

        return chossen_task
