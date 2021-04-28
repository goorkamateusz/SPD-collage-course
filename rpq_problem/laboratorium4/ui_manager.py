import sys
import getopt
from typing import List

from laboratorium4.algorithm import Algorithm
from laboratorium4.schrage_algorithm import SchrageAlgorithm
from laboratorium4.schrage_n_log_n import SchrageNLogNAlgorithm
from laboratorium4.schrage_pmtn import SchragePMTNAlgorithm
from laboratorium4.time_profiler import TimeProfiler


class UIManager:
    file_name = None
    _algorithm = []

    class Option:
        def __init__(self, short: str, long: str, description: str):
            self.short = short
            self.long = long
            self.description = description

        def __str__(self) -> str:
            short = self.short.replace(":", " arg")
            long = self.long.replace("=", "=arg")
            return f"{short}\t{long}\t - {self.description}"

    _options = [
        Option("f:", "file=", "nazwa pliku"),
        Option("h", "help", ""),
    ]

    @staticmethod
    def default_alg():
        UIManager._add_alg(SchrageAlgorithm())
        UIManager._add_alg(SchrageNLogNAlgorithm())
        UIManager._add_alg(SchragePMTNAlgorithm())

    @staticmethod
    def algorithms() -> List[Algorithm]:
        return UIManager.algorithms

    @staticmethod
    def load_sys_arg():
        arg_list = sys.argv[1:]
        options = "".join([opt.short for opt in UIManager._options])
        long_options = [opt.long for opt in UIManager._options]

        try:
            args, _ = getopt.getopt(arg_list, options, long_options)
            for curr_arg, curr_val in args:
                if curr_arg in ("-f", "--file"):
                    UIManager.file_name = curr_val

                if curr_arg in ("-h", "--help"):
                    UIManager.help()
                    exit()

        except getopt.error as err:
            print(str(err))
            exit()

        if UIManager.file_name is None:
            print("Nie podano nazwy pliku wejsciowego")
            exit()

        if not UIManager._algorithm:
            print("Nie wybrano algorytmu")

    @staticmethod
    def print(c_max: int, algorithm: Algorithm, profiler: TimeProfiler) -> None:
        print(algorithm.name)
        print(f"| C_max = {c_max}")
        print(f"| Czas obliczeń = {profiler}")

    @staticmethod
    def help() -> None:
        for op in UIManager._options:
            print(op)

    @staticmethod
    def _add_alg(alg: Algorithm) -> None:
        if alg not in UIManager._algorithm:
            UIManager._algorithm.append(alg)
