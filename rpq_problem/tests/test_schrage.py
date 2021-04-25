import pytest

from laboratorium4.algorithm import Algorithm
from laboratorium4.Cmax_calculator import CMaxCalculator
from laboratorium4.rpq_task_reader import RpqTaskReader
from laboratorium4.schrage_algorithm import SchrageAlgorithm
from laboratorium4.schrage_n_log_n import SchrageNLogNAlgorithm


@pytest.mark.parametrize('algorithm', [SchrageAlgorithm(), SchrageNLogNAlgorithm()])
@pytest.mark.parametrize('file_name,expected_value', [
    ('example_data/in50.txt', 1513),
    ('example_data/in100.txt', 3076),
    ('example_data/in200.txt', 6416),
])
def test_schrage(algorithm: Algorithm, file_name: str, expected_value: int):
    calculator = CMaxCalculator()
    tasks = RpqTaskReader.read(file_name)

    result = algorithm.run(tasks)
    C_max = calculator.get_Cmax(result)

    assert C_max == expected_value
