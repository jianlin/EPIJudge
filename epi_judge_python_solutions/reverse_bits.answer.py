from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    bm1 = 1
    bm2 = 1 << 63
    for i in range(32):
        if ((not (x & bm1)) != (not (x & bm2))):
            x = x ^ bm1 ^ bm2
        bm1 = bm1 << 1
        bm2 = bm2 >> 1
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
