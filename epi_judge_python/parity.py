from test_framework import generic_test
import sys

def parity(x: int) -> int:
    # TODO - you fill in here.
    p = 0
    while x != 0:
        p = ~p
        x = x & (x-1);
    return p & 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
