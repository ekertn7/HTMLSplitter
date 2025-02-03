"""Argument parser"""

import sys
import argparse


def create_argument_parser(
        default_max_len: int, default_file_path: str
    ) -> argparse.ArgumentParser:
    """Creates argument parser using argparse

    Args:
      --max-len [max_len]
        Argument to set up custom max length
      [file_path]
        Positional argumnet to choice file path

    Returns:
        An argparse argument parser object with arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--max-len', action='store', nargs='?', type=int,
                        default=default_max_len, required=False,
                        help='Set up custom max length')

    parser.add_argument('file_path', action='store', nargs='?', type=str,
                        default=default_file_path,
                        help='Choice file path')

    return parser.parse_args(sys.argv[1:])
