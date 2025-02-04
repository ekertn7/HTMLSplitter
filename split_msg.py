#!./venv/bin/python
"""Script to split origianl html into fixed length fragments"""

from config import DEFAULT_MAX_LEN, DEFAULT_FILE_PATH
from argument_parser.argument_parser import parse_command_line_arguments
from html_splitter.html_splitter import split_message


def main():
    """The main function"""
    namespace = parse_command_line_arguments(
        default_max_len=DEFAULT_MAX_LEN, default_file_path=DEFAULT_FILE_PATH)

    max_len = namespace.max_len
    file_path = namespace.file_path

    with open(file_path, 'r', encoding='utf-8') as file:
        source = file.read()

    fragment_number = 1
    for fragment in split_message(source, max_len):
        print(f'-- fragment #{fragment_number}: {len(fragment)} chars --')
        print(fragment)
        fragment_number += 1


if __name__ == "__main__":
    main()
