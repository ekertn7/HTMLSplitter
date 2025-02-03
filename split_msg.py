#!./venv/bin/python
"""Script to split html"""

import re
from typing import Generator
from bs4 import BeautifulSoup, Tag
from collections import defaultdict

from config import DEFAULT_MAX_LEN, DEFAULT_FILE_PATH
from argument_parser.argument_parser import create_argument_parser


def _replace_empty_tags(string: str) -> str:

    possible_block_tags = ['p', 'b', 'strong', 'i', 'ul', 'ol', 'div', 'span']

    pattern = '|'.join([fr'\<{tag}\>\s?\<\/{tag}\>\s?' for tag in possible_block_tags])

    return re.sub(f'({pattern})', '', string)


def _get_open_and_closed_tags(string: str) -> tuple[list[str], list[str]]:

    # find open and closed tags
    possible_block_tags = ['p', 'b', 'strong', 'i', 'ul', 'ol', 'div', 'span']
    open_block_tags_pattern = '|'.join([fr'\<{tag}\>' for tag in possible_block_tags])
    close_block_tags_pattern = '|'.join([fr'\<\/{tag}\>' for tag in possible_block_tags])

    open_tags = re.findall(f'({open_block_tags_pattern})', string)
    open_tags = [tag.replace('<', '').replace('>', '') for tag in open_tags]

    close_tags = re.findall(f'({close_block_tags_pattern})', string)
    close_tags = [tag.replace('<', '').replace('>', '').replace('/', '') for tag in close_tags]

    # remove already closed tags
    for item in open_tags.copy()[::-1]:
        if len(close_tags) != 0 and item == close_tags[0]:
            del open_tags[-1]
            del close_tags[0]

    result_open_tags = [f'<{tag}>' for tag in open_tags]
    result_close_tags = [f'</{tag}>' for tag in open_tags][::-1]

    return result_open_tags, result_close_tags


if __name__ == "__main__":
    namespace = create_argument_parser(
        default_max_len=DEFAULT_MAX_LEN, default_file_path=DEFAULT_FILE_PATH)

    max_len = namespace.max_len
    file_path = namespace.file_path

    with open(file_path, 'r', encoding='utf-8') as file:
        source = file.read()

    # html = BeautifulSoup(source, 'html.parser')

    delimeter_from = 0
    delimeter_to = delimeter_from + max_len

    saved_prefix = ''

    while True:
        print(delimeter_from, delimeter_to, len(source))

        source_chunk = saved_prefix + source[delimeter_from:delimeter_to]

        source_elements = re.findall(r'(\<.+)', source_chunk)

        if len(source_chunk) >= max_len:
            latest_element = source_elements.pop(-1)

        while True:
            unformatted_string = '\n'.join(source_elements) + '\n'

            unformatted_string = _replace_empty_tags(unformatted_string)

            open_tags, close_tags = _get_open_and_closed_tags(unformatted_string)

            prefix = '\n'.join(open_tags) + '\n'
            postfix = '\n'.join(close_tags)

            result_string = unformatted_string + postfix
            if len(result_string) <= max_len:
                break
            else:
                source_elements.pop(-1)

        print(len(result_string), result_string)

        if delimeter_to >= len(source):
            break
        delimeter_from = delimeter_from + len(unformatted_string) - len(saved_prefix)
        delimeter_to = delimeter_from + max_len
        saved_prefix = prefix
