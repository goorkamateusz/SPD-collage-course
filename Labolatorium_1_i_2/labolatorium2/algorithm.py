from timeit import default_timer as timer


class Algorithm:
    def __str__(self) -> str:
        return self.name

    def __eq__(self, oth) -> bool:
        return str(self) == str(oth)

    bench_time_us = 0

    def read_start_time(self):
        self.bench_time_us = timer()

    def read_end_time(self):
        self.bench_time_us = int((timer() - self.bench_time_us) * 1_000_000)
