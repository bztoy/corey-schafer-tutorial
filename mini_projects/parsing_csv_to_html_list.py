from utilities import (space, separated, start, end, sub, new_topic)
import os
import csv

# Key
key = 'mini_project_parsing_csv_field_to_an_html_tag_list'


def run():
    main()


def main():
    html_output = ''
    names = []

    file_path = os.path.join(
        os.getcwd(), 'mini_projects', 'patrons.csv')

    with open(file_path, 'r') as data_file:
        csv_data = csv.DictReader(data_file)

        # We don't want first line of bad data
        next(csv_data)
        next(csv_data)

        for line in csv_data:
            if line['FirstName'] == 'No Reward':
                break
            names.append(f"{line['FirstName']} {line['LastName']}")

    html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

    html_output += '\n<ul>'

    for name in names:
        html_output += f'\n\t<li>{name}</li>'

    html_output += '\n</ul>'
    print(html_output)
