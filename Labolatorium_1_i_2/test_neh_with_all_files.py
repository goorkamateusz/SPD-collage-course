from labolatorium2.NEH_algorithm import NehAlgorithm
from labolatorium2.neh_answer_reader import NehFileReader

import os

if __name__ == "__main__":
    pwd = os.path.dirname(__file__)
    dir = f"{pwd}/example_data/"

    for file in os.listdir(dir):
        try:
            neh_file = NehFileReader(f"{dir}/{file}")
            neh_file.verify_algorithm(NehAlgorithm())

        except AssertionError as err:
            print()
            print("-----------------------------")
            print(err)
            print("-----------------------------")
            print()
            input("Kliknij by uruchomic nastepny test")
