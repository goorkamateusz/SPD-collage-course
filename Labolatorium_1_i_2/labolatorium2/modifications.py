"""
    Źródło
    (1) http://dominik.zelazny.staff.iiar.pwr.wroc.pl/materialy/Algorytm_NEH_(Metoda_wstawien_w_klasycznych_problemach_szeregowania._Cz._I._Problem_przeplywowy).pdf
"""

from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task
from labolatorium2.critial_path import CritialPath


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
    """

        "Wśród zadań z permutacji π (z wyjątkiem zadania j) znajdź zadanie o
        największej liczbie operacji wchodzących w skład ścieŜki krytycznej w grafie G(π ) . JeŜeli
        wybór jest jednoznaczny, przyjmij to zadanie jako x. W przeciwnym wypadku jako zadanie
        x przyjmij zadanie, które jednocześnie ma największą wartość priorytetu (1)." (1)
    """
    name = "trzecia modyf."

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        # todo
        return sorted_tasks.popleft()


class FourthModification:
    """

        " Jako zadanie x przyjmij to zadanie z permutacji π (z wyjątkiem zadania j),
        którego usuniecie z tej permutacji spowoduje największe zmniejszenie wartości funkcji
        celu. " (1)
    """
    name = "czwarta modyf."

    def choose(self, sorted_tasks, optimal_task_list, gantt: Gantt) -> Task:
        # todo
        return sorted_tasks.popleft()
