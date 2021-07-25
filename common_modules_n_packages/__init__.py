from common_modules_n_packages.os import working_with_dir, environments_and_path
from common_modules_n_packages.datetimes import datetime_basic_date, datetime_basic_time, datetime_basic_formats
from common_modules_n_packages.files import read_files, write_files
from common_modules_n_packages.files.csv import parse_basic_csv, dict_reader_writer_csv
from common_modules_n_packages.randoms import randoms, random_demo
# from common_modules_n_packages.other_modules import randoms

# Key
key = 'common_modules_and_packages'

# Switch
sw = {
    # OS Module
    working_with_dir.key: False,
    environments_and_path.key: False,

    # Datetime Module
    datetime_basic_date.key: False,
    datetime_basic_time.key: False,
    datetime_basic_formats.key: False,

    # Files
    read_files.key: False,
    write_files.key: False,

    # CSV files
    parse_basic_csv.key: False,
    dict_reader_writer_csv.key: False,

    # Random modules
    randoms.key: False,
    random_demo.key: False

}


def run():
    # Working with DIR and Navigation
    if sw[working_with_dir.key]:
        working_with_dir.run()

    # System Environment and Path
    if sw[environments_and_path.key]:
        environments_and_path.run()

    # Datetime (Date)
    if sw[datetime_basic_date.key]:
        datetime_basic_date.run()

    # Datetime (Time)
    if sw[datetime_basic_time.key]:
        datetime_basic_time.run()

    # Datetime (format)
    if sw[datetime_basic_formats.key]:
        datetime_basic_formats.run()

    # Files (Read)
    if sw[read_files.key]:
        read_files.run()

    # Files (Write)
    if sw[write_files.key]:
        write_files.run()

    # CSV Files
    if sw[parse_basic_csv.key]:
        parse_basic_csv.run()

    if sw[dict_reader_writer_csv.key]:
        dict_reader_writer_csv.run()

    # Random Basic
    if sw[randoms.key]:
        randoms.run()

    # Random Demo
    if sw[random_demo.key]:
        random_demo.run()
