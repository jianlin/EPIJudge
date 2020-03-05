from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    #return 0

    if ( x & 1 == 1):  # has a 1 as rightmost bit   # ( (x + 1) & x == 0 ) can check for all 1's but not what we need here
        return (x + 1) + ((((x+1) & -(x+1)) - 1) >> 1)
    else:
        return x - 1 - (((x & -x) - 1) >> 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))

# from test_framework import generic_test


# def closest_int_same_bit_count(x: int) -> int:

#     num_unsigned_bits = 64
#     for i in range(num_unsigned_bits - 1):
#         if (x >> i) & 1 != (x >> (i + 1)) & 1:
#             x ^= (1 << i) | (1 << (i + 1))  # Swaps bit-i and bit-(i + 1).
#             return x

#     # Raise error if all bits of x are 0 or 1.
#     raise ValueError('All bits are 0 or 1')


# if __name__ == '__main__':
#     exit(
#         generic_test.generic_test_main('closest_int_same_weight.py',
#                                        'closest_int_same_weight.tsv',
#                                        closest_int_same_bit_count))
