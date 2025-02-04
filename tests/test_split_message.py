"""Tests of `split_message` function"""

import pytest
from config import DEFAULT_FILE_PATH
from app.html_splitter.html_splitter import split_message
from app.exceptions.exceptions import ImpossibleToSplitMessageException


@pytest.fixture(scope='function', autouse=False, name='source')
def prepare_source():
    """Fixture that read source file before tests"""
    with open(DEFAULT_FILE_PATH, 'r', encoding='utf-8') as file:
        source = file.read()
    return source


class TestsSplitMessage:
    """Tests of `split_message` function"""

    @pytest.mark.usefixtures('source')
    def test_exception_impossible_to_split_message(self, source):
        """Checks that throw exception when trying to split a message into too
        small fragments"""
        with pytest.raises(ImpossibleToSplitMessageException):
            next(split_message(source, max_len=1))

    @pytest.mark.usefixtures('source')
    @pytest.mark.parametrize(
        'max_len',
        [256, 512, 1024, 2048, 3076, 4096, 8192,]
    )
    def test_fragments_length(self, source, max_len):
        """Checks that length of all fragments less than or equal `max_len`"""
        assert all(
            len(fragment) <= max_len
            for fragment in split_message(source, max_len))

    @pytest.mark.usefixtures('source')
    @pytest.mark.parametrize(
        ['max_len', 'fragments_number'],
        [(256, 30),
         (512, 13),
         (1024, 6),
         (2048, 3),
         (3076, 2),
         (4096, 2),
         (8192, 1),
         ]
    )
    def test_fragments_number(self, source, max_len, fragments_number):
        """Checks that the number of fragments is equal to `fragments_number`"""
        assert len(list(split_message(source, max_len))) == fragments_number
