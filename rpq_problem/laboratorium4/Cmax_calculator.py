from typing import List

from laboratorium4.task import Task


class CMaxCalculator:
    """
    Kalkulator liczący C_max dla podanej permutacji tasków.
    """
    def get_Cmax(self, tasks_list: List[Task]) -> int:
        # Momenty rozpoczęcia wykonywania zadań
        S = [tasks_list[0].get_preparation_time()]

        for i in range(1, len(tasks_list)):
            previous_task = tasks_list[i - 1]
            current_task = tasks_list[i]
            S.append(max(current_task.get_preparation_time(), S[i-1] + previous_task.get_execution_time()))

        # Momenty zakończenia wykonywania zadań
        C = []
        for task_start_time, task in zip(S, tasks_list):
            C.append(task_start_time + task.get_execution_time())

        # Czasy zakończenia i dostarczenia wszystkich zadań
        completion_and_delivery_times = []
        for task_completion_time, task in zip(C, tasks_list):
            completion_and_delivery_times.append(task_completion_time + task.get_delivery_time())

        return max(completion_and_delivery_times)
