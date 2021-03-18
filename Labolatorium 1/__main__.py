from labolatorium1.all_possibilities import AllPossibilities
from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task, Machine
from labolatorium1.silly_algorithm import SillyAlgorithm
from labolatorium1.johnson_rule import JohnsonRule

def display_and_print_out(Machines: list) -> None:
    for machine in machines_with_task:
        print(machine)

    gantt = Gantt(machines_with_task)
    print(f"Czas trwania {gantt.get_duration()}")
    gantt.plot()

if __name__ == "__main__":

    # import danych
    # tasks = [Task(i) for i in range(1, 6)]
    # A = Machine(1)
    # B = Machine(2)
    # C = Machine(3)

    # time_A = [4, 4, 10, 6, 2]
    # time_B = [5, 1, 4, 10, 3]
    # time_C = [2, 3, 5, 2, 4]

    tasks = [Task(i) for i in range(1, 5)]
    A = Machine(1)
    B = Machine(2)
    C = Machine(3)

    time_A = [1, 9, 7, 4]
    time_B = [3, 3, 8, 8]
    time_C = [8, 5, 6, 7]

    for i in range(len(tasks)):
        task = tasks[i]
        A.add_task_duration(task, time_A[i])
        B.add_task_duration(task, time_B[i])
        C.add_task_duration(task, time_C[i])

    # permutacja
    algorithm = AllPossibilities()
    copy = [m.copy_without_task_queue() for m in [A, B, C]]
    machines_with_task = algorithm.run(copy, tasks)
    display_and_print_out(machines_with_task)

    # algorytm Johnsona
    algorithm = JohnsonRule()
    copy = [m.copy_without_task_queue() for m in [A, B, C]]
    machines_with_task = algorithm.run(copy, tasks)
    display_and_print_out(machines_with_task)
