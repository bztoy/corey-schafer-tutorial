from mini_projects import auto_parse_rename_multi_files, parsing_csv_to_html_list

# Key
key = 'mini_projects'

# Switch
sw = {
    # Automate Parsing and Renaming of Multiple Files
    auto_parse_rename_multi_files.key: False,
    parsing_csv_to_html_list.key: True
}


def run():
    # Working with DIR and Navigation
    if sw[auto_parse_rename_multi_files.key]:
        auto_parse_rename_multi_files.run()

    # Real World Example - Parsing Names From a CSV to an HTML List
    if sw[parsing_csv_to_html_list.key]:
        parsing_csv_to_html_list.run()
