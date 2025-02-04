"""Module with functions to split html"""

import re
from typing import Generator
from collections import Counter


POSSIBLE_BLOCK_TAGS = ['p', 'b', 'strong', 'i', 'ul', 'ol', 'div', 'span']


def _find_open_tags(fragment: str) -> str:
    """Finds all open tags in fragment"""

    open_block_tags_pattern = \
        '|'.join([fr'\<{tag}\>' for tag in POSSIBLE_BLOCK_TAGS])

    open_tags = re.findall(f'({open_block_tags_pattern})', fragment)
    open_tags = [tag.replace('<', '').replace('>', '') for tag in open_tags]

    return open_tags


def _find_close_tags(fragment: str) -> str:
    """Finds all close tags in fragment"""

    close_block_tags_pattern = \
        '|'.join([fr'\<\/{tag}\>' for tag in POSSIBLE_BLOCK_TAGS])

    close_tags = re.findall(f'({close_block_tags_pattern})', fragment)
    close_tags = [
        tag.replace('<', '').replace('>', '').replace('/', '')
        for tag in close_tags]
    close_tags = close_tags[::-1]

    return close_tags


def _get_open_and_close_tags(fragment: str) -> tuple[list[str], list[str]]:
    """Finds open and close tags in fragment

    Parameters
    ----------
    fragment
        An input HTML fragment

    Returns
    -------
        A tuple with:
            - list of open tags in correct order
            - list of close tags in correct order
    """

    # find open and close tags
    open_tags = _find_open_tags(fragment)
    close_tags = _find_close_tags(fragment)

    # remove already closed tags
    c_open_tags = Counter(open_tags)
    c_close_tags = Counter(close_tags)
    diff = list((c_open_tags - c_close_tags).elements())

    # postprocess result
    result_open_tags = [f'<{tag}>' for tag in diff]
    result_close_tags = [f'</{tag}>' for tag in diff][::-1]

    return result_open_tags, result_close_tags


def _remove_empty_tags(fragment: str) -> str:
    """Removes empty tags from fragment"""

    pattern = '|'.join([fr'\<{tag}\>\s?\<\/{tag}\>\s?' for tag in POSSIBLE_BLOCK_TAGS])

    iterations = len(_find_open_tags(fragment))
    for _ in range(iterations):
        fragment = re.sub(f'({pattern})', '', fragment)

    return fragment


def split_message(source: str, max_len: int) -> Generator[str]:
    """Splits the original message (`source`) into fragments of the specified
    length (`max_len`)

    Parameters
    ----------
    source
        Original message
    max_len
        Max result fragment length

    Yields
    ------
        Result fragment
    """

    source = re.sub(r'\n+', '\n', source)  # remove double \n
    source = re.sub(r'\n$', '', source)  # remove last \n

    source_elements = re.findall(r'(.+\n)', source)

    accumulator = ''
    prefix = ''
    for idx, chunk in enumerate(source_elements):
        open_tags, close_tags = _get_open_and_close_tags(accumulator + chunk)
        prefix = '\n'.join(open_tags) + '\n'
        postfix = '\n'.join(close_tags)

        if len(accumulator) + len(chunk) + len(postfix) <= max_len:
            accumulator = accumulator + chunk

        if not (len(accumulator) + len(chunk) + len(postfix) <= max_len) or \
                (idx + 1 == len(source_elements)):
            result = _remove_empty_tags(accumulator + postfix)
            if len(result) != 0:
                yield result
                accumulator = prefix
