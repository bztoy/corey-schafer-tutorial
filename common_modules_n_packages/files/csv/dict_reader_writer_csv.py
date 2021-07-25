from utilities import (space, separated, start, end, sub, new_topic)
import csv
import os

# Key
key = 'files_csv_dict_reader'


def run():
    start('CSV File: Dictionary Reader')
    new_topic('Read File into a Dict')
    # Change Working Dir
    original_file = os.path.join(
        os.getcwd(), 'common_modules_n_packages', 'files', 'csv', 'names.csv')
    new_file = os.path.join(
        os.getcwd(), 'common_modules_n_packages', 'files', 'csv', 'new_names_dict.csv')

    with open(original_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            print(line)

    new_topic('Write File with DictWriter')
    with open(original_file, 'r') as csv_file, open(new_file, 'w', newline='') as csv_new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        csv_reader = csv.DictReader(csv_file)
        csv_writer = csv.DictWriter(
            csv_new_file, fieldnames=fieldnames, delimiter='\t')
        # Write header
        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
    print(f'file {new_file} created!')

    new_topic('Write File with DictWriter - Modify field list')
    new_file = os.path.join(
        os.getcwd(), 'common_modules_n_packages', 'files', 'csv', 'modify_names_dict.csv')
    with open(original_file, 'r') as csv_file, open(new_file, 'w', newline='') as csv_new_file:
        fieldnames = ['first_name', 'last_name']
        csv_reader = csv.DictReader(csv_file)
        csv_writer = csv.DictWriter(
            csv_new_file, fieldnames=fieldnames, delimiter='\t')
        # Write header
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
    print(f'file {new_file} created!')

    end()
