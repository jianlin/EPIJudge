from test_framework import generic_test


def count_bits(x: int) -> int:
    # TODO - you fill in here.
    c = 0
    while x:
        x = x & (x - 1)
        c += 1
    return c


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
