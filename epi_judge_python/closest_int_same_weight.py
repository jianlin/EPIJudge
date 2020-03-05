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
