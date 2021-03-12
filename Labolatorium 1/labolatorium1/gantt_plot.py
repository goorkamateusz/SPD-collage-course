import matplotlib.pyplot as plt
from labolatorium1.general_lib import Machine, Task

class TaskTime:
        """
        Klasa przechowujaca czas wykonania i czas trwania taska
        """
        def __init__(self, task: Task, start: int, duration: int) -> None:
            self.task = task
            self.start = start
            self.duration = duration
            self.finish = start+duration

        def get_id(self) -> int:
            return self.task.get_id()


class Gantt:
    """
    Wykonuje wszystkie niezbędne obliczenia nad rozkładem w czasie zadań na maszynach
    """
    def __init__(self, machines: list) -> int:
        self.machines = machines
        self.duration = 0
        self.__calculate()

    def __calculate(self):
        """
        Uzupełnia listę time_line w machines klasami `TaskTime`, zawierajacymi początek i czas trwania taska.
        """
        raise NotImplementedError()


    def plot(self):
        plot = Gantt.Plot(self.machines, self.duration)
        plot.show()

    class Plot:
        colors = ["red", "blue", "green", "orange"]

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
                            [(task.start, task.finish)],
                            (self.y_pos(machine_id), 1),
                            facecolors = (f"tab:{self.colors[self.color_id(task.get_id())]}")
                        )

        def _set_limit(self):
            self.gnt.set_ylim(0, (len(self.__machines) + 1))
            self.gnt.set_xlim(0, self._get_c_max())

        def _set_labels(self):
            self.gnt.set_xlabel("Time")
            self.gnt.set_ylabel("Machines")

        def _set_ticks(self):
            self.gnt.set_yticks([(i+1) for i in range(len(self.__machines))])
            self.gnt.set_yticklabels([f"{m.get_id()}" for m in self.__machines])

        def _get_c_max(self):
            return self.__duration

        def y_pos(self, machine_id) -> int:
            return (machine_id+0.5)

        def color_id(self) -> int:
            self.__color_i = (self.__color_i + 1) % len(self.colors)
            return self.__color_i

        def color_id(self, id: int) -> int:
            return (id) % len(self.colors)
