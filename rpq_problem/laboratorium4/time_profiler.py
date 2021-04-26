from timeit import default_timer as timer


class TimeProfiler:
    class StateCode:
        NOT_INIT = -1
        STARTED = 0
        FINISHED = 1

    def __init__(self) -> None:
        self.__state = TimeProfiler.StateCode.NOT_INIT
        self.__bench_time_us = None

    def __str__(self) -> str:
        try:
            return str(self.get_duration())
        except Exception as ex:
            return str(ex)

    def get_duration(self) -> int:
        if self.__state > 0:
            return self.__bench_time_us
        else:
            raise Exception("Nie zakonczono pomiaru czasu")

    def start(self):
        self.__state = TimeProfiler.StateCode.STARTED
        self.__bench_time_us = timer()

    def stop(self):
        if self.__state < 0:
            raise Exception("Nie zainicjalizowany timer")
        self.__state = TimeProfiler.StateCode.FINISHED
        self.__bench_time_us = int((timer() - self.__bench_time_us) * 1_000_000)
