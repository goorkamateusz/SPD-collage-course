from labolatorium1.general_lib import Task, Machine

class TaskTime(Task):
    def __init__(self, task: Task, start: int, duration: int) -> None:
        super().__init__(task._id)
        self.start = start
        self.duration = duration
        self.finish = start+duration

class AllTaskAreCalculated(Exception):
    pass

class MachineTime(Machine):
    def __init__(self, machine: Machine) -> None:
        super().__init__(machine.get_id())
        self.tasks = machine.tasks
        self._tasks_durations = machine._tasks_durations
        self.time_line = []

    def get_finish_time(self) -> int:
        if len(self.time_line) == 0:
            return 0
        else:
            return self.time_line[-1].finish

    def get_first_not_calculated_task(self) -> Task:
        if len(self.tasks) == len(self.time_line):
            raise AllTaskAreCalculated()
        return self.tasks[len(self.time_line)]

    def add_task(self, task: Task, start_time: int) -> None:
        duration = self.get_task_duration(task)
        self.time_line.append(TaskTime(task, start_time, duration))
