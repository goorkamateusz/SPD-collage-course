#!/usr/bin/python3
import job_shop

def job_shop_ortools(file_path):
    test_instance = job_shop.load_from_file(file_path)
    cmax, pi_order, status = job_shop.job_shop_ortools(test_instance)
    print(f"Cmax: {cmax}\norder: {pi_order}\n{status}")

if __name__ == "__main__":
    
    job_shop_ortools("Mkh_splitter/insa.data.txt")