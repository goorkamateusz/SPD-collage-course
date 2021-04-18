from timeit import default_timer as timer

class StopConditions:
    def start(self) -> None:
        pass

    def contnue(self, c_max: int) -> None:
        pass


class TimeCondition(StopConditions):
    def __init__(self, max_duration: float) -> None:
        super().__init__()
        self.time_start = None
        self.duration = max_duration

    def start(self) -> None:
        self.time_start = timer()

    def contnue(self, c_max: int) -> None:
        return timer() - self.time_start > self.duration


class IterCondition(StopConditions):
    def __init__(self, max_iter: int) -> None:
        self.iter = max_iter

    def contnue(self, c_max: int) -> None:
        self.iter -= 1
        return self.iter > 0
