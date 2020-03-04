from test_framework import generic_test


# def count_bits(x: int) -> int:
#     # TODO - you fill in here.
#     c = 0
#     while x:
#         x = x & (x - 1)
#         c += 1
#     # return c 
#     return 0


def count_bits(x: int) -> int:

    # num_bits = 0
    # while x:
    #     num_bits += x & 1
    #     x >>= 1
    # return num_bits
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
