from test_framework import generic_test


def swap_bits(x, i, j):
    # TODO - you fill in here.
    bm1 = 1 << i
    bm2 = 1 << j
    if ( (not (x & bm1)) !=  (not (x & bm2))):
        x = x ^ bm1 ^ bm2
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
