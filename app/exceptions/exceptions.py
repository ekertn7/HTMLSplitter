"""Splitter exceptions"""


class SplitterException(Exception):
    """Base splitter exception"""
    def __init__(self, message: str):
        super().__init__()
        self._message = message

    def __str__(self):
        return self._message


class ImpossibleToSplitMessageException(SplitterException):
    """Exception when impossible to split message"""
    def __init__(self):
        message = (
            'It\'s impossible to split message because the `max_len` parameter '
            'is too low!')
        super().__init__(message)
