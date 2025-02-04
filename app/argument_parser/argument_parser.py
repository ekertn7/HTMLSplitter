"""Module with function to parse command line arguments"""

import sys
import argparse


def parse_command_line_arguments(
        default_max_len: int, default_file_path: str
    ) -> argparse.ArgumentParser:
    """Creates argument parser using argparse and returns namespace

    Args:
      --max-len [max_len]
        Argument to set up custom max length
      [file_path]
        Positional argumnet to choice file path

    Returns:
        Namespace with parsed arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--max-len', action='store', nargs='?', type=int,
                        default=default_max_len, required=False,
                        help='Set up custom max length')

    parser.add_argument('file_path', action='store', nargs='?', type=str,
                        default=default_file_path,
                        help='Choice file path')

    namespace = parser.parse_args(sys.argv[1:])

    return namespace
