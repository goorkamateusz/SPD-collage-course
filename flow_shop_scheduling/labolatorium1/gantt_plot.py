import matplotlib.pyplot as plt
from labolatorium1.general_lib import Machine, Task
from labolatorium1.calculable_lib import AllTaskAreCalculated, MachineDescribed, TaskAssigned
from labolatorium2.critial_path import CritialPath

from typing import List

class Gantt:
    """
    Wykonuje wszystkie niezbędne obliczenia nad rozkładem w czasie zadań na maszynach.

    W konstruktorze dostaje listę maszyn `Machine` z uzupełnionym czasem trawnia zadań i listą zadań.
    - `plot()` Pozwala rysować wykresy;
    - `get_duration()` Zwaca czas trawnia całego procesue;

    """
    def __init__(self, machines: List[Machine]) -> None:
        self.machines = list(map(MachineDescribed, machines))
        # self.__assert_me()
        self.__duration = 0
        self.critical_path = CritialPath()
        self.__calculate()

    def __calculate(self):
        """
        Uzupełnia listę time_line w machines klasami `TaskTime`, zawierajacymi początek i czas trwania taska.
        """
        finish = False
        task_ending_moment = {}

        while not finish:
            finish = True
            current_tasks = []
            for machine in self.machines:
                try:
                    task = machine.get_first_not_calculated_task()

                    finish = False

                    if task not in current_tasks:
                        if task in task_ending_moment:
                            start_time = max(task_ending_moment[task], machine.get_finish_time())
                        else:
                            start_time = machine.get_finish_time()

                        task_time = machine.add_task(task, start_time)
                        finish_time = machine.get_finish_time()

                        current_tasks.append(task)
                        task_ending_moment[task] = finish_time
                        self.critical_path.add(task_time)

                except AllTaskAreCalculated:
                    continue

        self.__duration = max([m.get_finish_time() for m in self.machines])

    def __assert_me(self):
        for i in range(1, len(self.machines)):
            if self.machines[i].get_number_of_tasks() == self.machines[i-1].get_number_of_tasks():
                assert "gdzies usunieto taska"
        print(f"ilosc maszyn: {len(self.machines)}")
        print(f"ilosc zadan: {self.machines[i].get_number_of_tasks()}")

    def get_duration(self) -> int:
        return self.__duration

    def get_critical_path(self) -> List[TaskAssigned]:
        return self.critical_path.get_path()

    def plot(self, plot_name: str):
        plot = Gantt.Plot(self)
        plot.plot(plot_name)

    class Plot:
        colors = [
            "olive",
            "blue",
            "orange",
            "green",
            "red",
            "purple",
            "pink",
            "gray",
            "cyan",
            "brown"
        ]

        def __init__(self, gantt):
            self.__critical_path = gantt.get_critical_path()
            self.__machines = gantt.machines
            self.__duration = gantt.get_duration()
            self.__color_i = 0
            _, self.gnt = plt.subplots()
            self._set_limit()
            self._set_labels()
            self._set_ticks()
            self._draw_plot()

        def plot(self, plot_name = "Bez nazwy"):
            self.gnt.set_title(plot_name)
            plt.plot()

        @staticmethod
        def show() -> None:
            plt.show()

        def _draw_plot(self):
            self.gnt.grid(True)

            for machine_id in range(len(self.__machines)):
                for task in self.__machines[machine_id].time_line:
                    on_critical_path = task.is_on_the_path(self.__critical_path)
                    self.gnt.broken_barh(
                            [(task.start, task.duration)],
                            (self.y_pos(machine_id), 1),
                            facecolors = (f"tab:{self.colors[self.color_id(task.get_id())]}"),
                            edgecolors = "white" if on_critical_path else "face",
                            url = task.get_id()
                        )

                    self.gnt.text(
                            x = task.start + task.duration/2,
                            y = self.y_pos(machine_id) + 0.5,
                            s = f"{task.get_id()}\n({task.duration})",
                            ha = 'center',
                            va = 'center',
                            color = 'white' if on_critical_path else "black",
                        )

        def _set_limit(self):
            self.gnt.set_ylim(0, (len(self.__machines) + 1))
            self.gnt.set_xlim(0, self._get_c_max())

        def _set_labels(self):
            self.gnt.set_xlabel(f"Time [czas trawnia: {self.__duration}]")
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
