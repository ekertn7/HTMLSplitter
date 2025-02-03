#!./venv/bin/python
"""Script to split html"""

from typing import Generator
from bs4 import BeautifulSoup

from config import DEFAULT_MAX_LEN, DEFAULT_FILE_PATH
from argument_parser.argument_parser import create_argument_parser


def split_message(source: str, max_len: int):  # -> Generator[str]:
    """Splits the original message `source` into fragments of the specified
    length `max_len`
    """
    html = BeautifulSoup(source, 'html.parser')
    accumulated_elements = ''

    for selected_element in html.find_all():
        if len(str(accumulated_elements)) + len(str(selected_element)) <= max_len:
            accumulated_elements += str(selected_element)
        else:
            print(accumulated_elements)
            if len(str(selected_element)) <= max_len:
                accumulated_elements = str(selected_element)
            else:
                print('--OOOOPS--')
                print(selected_element)
            print('\n--------\n')

    # start = 0
    # end = max_len

    # while True:
    #     if start >= len(source):
    #         break
    #     chunk = source[start:end]
    #     yield chunk
    #     start += max_len
    #     end += max_len


def search(source: str, close_tags: str = '', max_len: int = DEFAULT_MAX_LEN):
    # базовый случай = вернет массив (когда длина (текущего элемента + предыдущего + закрывающих тегов) < max_len)
    # рекурсивный случай = уйдет в рекурсию (строка + закрывающий тег)
    all_items = BeautifulSoup(source, 'html.parser')

    try:
        extracted_item = all_items.find_all()[0].extract()
    except IndexError:
        return ''

    if len(str(extracted_item)) + accumulated_item <= max_len:

    # if len(accumulator) + len(str(extracted_tag)) <= max_len:
    #     accumulator += str(extracted_tag)
    #     return accumulator
    #     # return search(item=tags, accumulator=accumulator)

    # if len(accumulator) + len(str(extracted_tag)) > max_len:
    #     return search(item=tags, accumulator='')


if __name__ == "__main__":
    namespace = create_argument_parser(
        default_max_len=DEFAULT_MAX_LEN, default_file_path=DEFAULT_FILE_PATH)

    max_len = namespace.max_len
    file_path = namespace.file_path

    with open(file_path, 'r', encoding='utf-8') as file:
        source = file.read()

    split_message(source=source, max_len=max_len)

    # for item in search(source=source):
    #     print(item)
    #     print('----------\n')

    print(search(source=source))

    # for item in split_message(source=source, max_len=max_len):
    #     print(item)
    #     print()
    #     print('----------------------')
    #     print()
