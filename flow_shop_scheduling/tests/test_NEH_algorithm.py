from labolatorium2.neh_answer_reader import NehFileReader
from labolatorium2.NEH_algorithm import NehAlgorithm

import os
dirname = os.path.dirname(__file__)

def test_basic_data():
    file_name = f"{dirname}/../example_data/data.000"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithm())

def test_basic_data_2():
    file_name = f"{dirname}/../example_data/data.001"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithm())
