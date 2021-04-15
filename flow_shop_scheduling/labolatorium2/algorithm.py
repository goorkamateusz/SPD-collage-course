from timeit import default_timer as timer
from typing import List

from labolatorium1.general_lib import Machine, Task


class Algorithm:
    def run(self, machines: List[Machine], tasks: List[Task]) -> List[Machine]:
        raise NotImplementedError()

    def __str__(self) -> str:
        return self.name

    def __eq__(self, oth) -> bool:
        return str(self) == str(oth)

    def read_start_time(self):
        self.bench_time_us = timer()

    def read_end_time(self):
        self.bench_time_us = int((timer() - self.bench_time_us) * 1_000_000)
