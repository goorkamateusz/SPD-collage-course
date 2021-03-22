import matplotlib.pyplot as plt
from labolatorium1.general_lib import Machine, Task
from labolatorium1.calculable_lib import AllTaskAreCalculated, MachineTime, TaskTime


class Gantt:
    """
    Wykonuje wszystkie niezbędne obliczenia nad rozkładem w czasie zadań na maszynach.

    W konstruktorze dostaje listę maszyn `Machine` z uzupełnionym czasem trawnia zadań i listą zadań.
    - `plot()` Pozwala rysować wykresy;
    - `get_duration()` Zwaca czas trawnia całego procesue;

    """
    def __init__(self, machines: list) -> None:
        self.machines = []
        for machine in machines:
            self.machines.append(MachineTime(machine))
        self.__duration = 0
        self.__calculate()

    def __calculate(self):
        """
        Uzupełnia listę time_line w machines klasami `TaskTime`, zawierajacymi początek i czas trwania taska.
        """
        finish = False
        task_ending_moment = {}

        while not finish:
            finish = True
            current_task = []
            for machine in self.machines:
                try:
                    task = machine.get_first_not_calculated_task()

                    finish = False

                    if task not in current_task:
                        if task in task_ending_moment:
                            start_time = max(task_ending_moment[task], machine.get_finish_time())
                        else:
                            start_time = machine.get_finish_time()

                        machine.add_task(task, start_time)
                        finish_time = machine.get_finish_time()

                        current_task.append(task)
                        task_ending_moment[task] = finish_time

                except AllTaskAreCalculated:
                    continue

        self.__duration = max([m.get_finish_time() for m in self.machines])

    def get_duration(self) -> int:
        return self.__duration

    def plot(self):
        plot = Gantt.Plot(self.machines, self.__duration)
        plot.show()

    class Plot:
        colors = [
            "blue",
            "orange",
            "green",
            "red",
            "purple",
            "pink",
            "gray",
            "olive",
            "cyan",
            "brown"
        ]

        def __init__(self, machines: list, duration: int):
            self.__machines = machines
            self.__color_i = 0
            self.__duration = duration
            _, self.gnt = plt.subplots()
            self._set_limit()
            self._set_labels()
            self._set_ticks()
            self._draw_plot()

        def show(self):
            plt.show()

        def _draw_plot(self):
            self.gnt.grid(True)
            c_id = 0

            for machine_id in range(len(self.__machines)):
                for task in self.__machines[machine_id].time_line:
                    self.gnt.broken_barh(
                            [(task.start, task.duration)],
                            (self.y_pos(machine_id), 1),
                            facecolors = (f"tab:{self.colors[self.color_id(task.get_id())]}"),
                            url = task.get_id()
                        )

                    self.gnt.text(
                            x = task.start + task.duration/2,
                            y = self.y_pos(machine_id) + 0.5,
                            s = f"{task.get_id()}\n({task.duration})",
                            ha = 'center',
                            va = 'center',
                            color = 'white',
                        )

        def _set_limit(self):
            self.gnt.set_ylim(0, (len(self.__machines) + 1))
            self.gnt.set_xlim(0, self._get_c_max())

        def _set_labels(self):
            self.gnt.set_xlabel("Time")
            self.gnt.set_ylabel("Machines")

        def _set_ticks(self):
            self.gnt.set_yticks([i for i in range(len(self.__machines), 0, -1)])
            self.gnt.set_yticklabels([f"{m.get_id()}" for m in self.__machines])

        def _get_c_max(self):
            return self.__duration

        def y_pos(self, machine_id) -> int:
            return (len(self.__machines) - machine_id - 0.5)

        def color_id(self) -> int:
            self.__color_i = (self.__color_i + 1) % len(self.colors)
            return self.__color_i

        def color_id(self, id: int) -> int:
            return (id) % len(self.colors)
