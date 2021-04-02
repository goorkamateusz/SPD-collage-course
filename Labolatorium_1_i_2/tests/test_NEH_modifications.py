from labolatorium2.NEH_algorithm_modification import NehAlgorithmModification
from labolatorium2.without_modification import WithoutModification
from labolatorium2.modifications import *
from labolatorium2.neh_answer_reader import NehFileReader

import os
dirname = os.path.dirname(__file__)

def test_without_modification():
    file_name = f"{dirname}/../example_data/data.000"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(WithoutModification()))

def test_without_modification_1():
    file_name = f"{dirname}/../example_data/data.001"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(WithoutModification()))

def test_first_modification():
    file_name = f"{dirname}/../example_data/data.002"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(FirstModification()))

def test_first_modification():
    file_name = f"{dirname}/../example_data/data.001"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(FirstModification()))

def test_sec_modification():
    file_name = f"{dirname}/../example_data/data.002"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(SecondModification()))

def test_sec_modification():
    file_name = f"{dirname}/../example_data/data.001"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(SecondModification()))

def test_th_modification():
    file_name = f"{dirname}/../example_data/data.002"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(ThirdModification()))

def test_th_modification():
    file_name = f"{dirname}/../example_data/data.001"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(ThirdModification()))

def test_fo_modification():
    file_name = f"{dirname}/../example_data/data.002"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(FourthModification()))

def test_foth_modification():
    file_name = f"{dirname}/../example_data/data.001"
    neh_file = NehFileReader(file_name)
    neh_file.verify_algorithm(NehAlgorithmModification(FourthModification()))
