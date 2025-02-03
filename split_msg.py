#!./venv/bin/python
"""Script to split html"""

from typing import Generator
from bs4 import BeautifulSoup, Tag

from config import DEFAULT_MAX_LEN, DEFAULT_FILE_PATH
from argument_parser.argument_parser import create_argument_parser


def search(source: list[Tag]) -> list[Tag]:
    if sum(len(i) for i in source) >= max_len:
        return search(source[0]) + search(source[1:])
    else:
        return source


if __name__ == "__main__":
    namespace = create_argument_parser(
        default_max_len=DEFAULT_MAX_LEN, default_file_path=DEFAULT_FILE_PATH)

    max_len = namespace.max_len
    file_path = namespace.file_path

    with open(file_path, 'r', encoding='utf-8') as file:
        source = file.read()

    html = BeautifulSoup(source, 'html.parser').find_all()

    print(search(source=html))

    # html.descendant
