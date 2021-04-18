from timeit import default_timer as timer
import math
from typing import List

class StopConditions:
    def __init__(self) -> None:
        self.name = None

    def start(self) -> None:
        pass

    def stop(self, c_max: int) -> None:
        pass

    def __str__(self) -> str:
        return self.name


class TimeCondition(StopConditions):
    def __init__(self, max_duration: float) -> None:
        super().__init__()
        self.time_start = None
        self.duration = max_duration
        self.name = f"max time {max_duration}"

    def start(self) -> None:
        self.time_start = timer()

    def stop(self, c_max: int) -> None:
        return (timer() - self.time_start) > self.duration


class IterCondition(StopConditions):
    def __init__(self, max_iter: int) -> None:
        self.iter = max_iter
        self.name = f"max iter {max_iter}"

    def stop(self, c_max: int) -> None:
        self.iter -= 1
        return self.iter < 0


class WithoutProgresCondition(StopConditions):
    def __init__(self, max_no_progres_iter: int) -> None:
        self.max_no_progres_iter = max_no_progres_iter
        self.no_progres_iter = 0
        self.last_better_cmax = math.inf
        self.name = f"without progress {max_no_progres_iter}"

    def stop(self, c_max: int) -> None:
        if c_max < self.last_better_cmax:
            self.no_progres_iter = 0
            self.last_better_cmax = c_max
            return False
        else:
            self.no_progres_iter += 1
            return self.no_progres_iter > self.max_no_progres_iter


class ComplexStopCondition(StopConditions):
    def __init__(self, conditions: List[StopConditions]) -> None:
        self.conditions = conditions
        self.name = " & ".join([c.name for c in conditions])

    def start(self) -> None:
        for c in self.conditions:
            c.start()

    def stop(self, c_max: int) -> None:
        for c in self.conditions:
            if c.stop(c_max):
                return True
        return False
