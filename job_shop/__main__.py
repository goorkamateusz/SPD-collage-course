#!/usr/bin/python3
import job_shop

if __name__ == "__main__":

    test_instance = job_shop.load_from_file("Mkh_splitter/insa.data.txt")
    job_shop.job_shop_ortools(test_instance)