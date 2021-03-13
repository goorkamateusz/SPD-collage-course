from labolatorium1.gantt_plot import Gantt
from labolatorium1.general_lib import Task, Machine
from labolatorium1.silly_algorithm import SillyAlgorithm

if __name__ == "__main__":
    # import danych
    tasks = [Task(i) for i in range(1,6)]
    A = Machine(1)
    B = Machine(2)

    time_A = [4, 4, 10, 6, 2]
    time_B = [5, 1, 4, 10, 3]
    for i in range(len(tasks)):
        task = tasks[i]
        A.add_task_duration(task, time_A[i])
        B.add_task_duration(task, time_B[i])

    # algorytm
    algorithm = SillyAlgorithm()
    machines_with_task = algorithm.run([A, B], tasks)

    # wyswietlenie i obliczenia
    for machine in machines_with_task:
        print(machine)

    gantt = Gantt(machines_with_task)
    print(f"Czas trwania{gantt.get_duration()}")
    gantt.plot()
