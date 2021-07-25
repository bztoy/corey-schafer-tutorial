from utilities import (space, separated, start, end, sub, new_topic)
import csv
import os

# Key
key = 'files_csv_parse_basic'


def run():
    start('CSV File: Parsing')
    new_topic('Read File')

    # Change Working Dir
    original_file = os.path.join(
        os.getcwd(), 'common_modules_n_packages', 'files', 'csv', 'names.csv')
    new_file = os.path.join(
        os.getcwd(), 'common_modules_n_packages', 'files', 'csv', 'new_names.csv')

    with open(original_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Skip the first line
        next(csv_reader)

        for line in csv_reader:
            print(line)

    new_topic('Write File', True)
    with open(original_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        with open(new_file, 'w', newline='') as csv_new_file:
            delimiter = '\t'  # Tab
            csv_writer = csv.writer(csv_new_file, delimiter=delimiter)

            for line in csv_reader:
                csv_writer.writerow(line)
        print(f'file {new_file} created!')

    new_topic('Read file, specify delimeter', True)
    read_new_file = os.path.join(
        os.getcwd(), 'common_modules_n_packages', 'files', 'csv', 'new_names_tab.csv')
    with open(read_new_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        # Skip the first line
        next(csv_reader)

        for line in csv_reader:
            print(line)

    end()
