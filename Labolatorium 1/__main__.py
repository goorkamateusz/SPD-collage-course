# from labolatorium1.johnson_rule import *
# from labolatorium1.all_possibilities import *
from labolatorium1.gantt_plot import *

if __name__ == "__main__":
    tasks = [Task(i) for i in range(1,6)]
    A = Machine(1)
    B = Machine(2)

    time_A = [4, 4, 10, 6, 2]
    time_B = [5, 1, 4, 10, 3]
    for i in range(len(tasks)):
        task = tasks[i]
        A.add_task_duration(task, time_A[i])
        B.add_task_duration(task, time_B[i])
        A.add_task(task)
        B.add_task(task)

    print(A)
    print(B)

    gantt = Gantt([A, B])
    # gantt = Gantt([A])
    print(gantt.duration)
    gantt.plot()

    pass
