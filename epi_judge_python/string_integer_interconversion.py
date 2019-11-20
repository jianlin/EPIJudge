from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    return ''


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    return 0


def wrapper(x, s):
    try:
        if int(int_to_string(x)) != x:
            raise TestFailure('Int to string conversion failed')
    except ValueError:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
