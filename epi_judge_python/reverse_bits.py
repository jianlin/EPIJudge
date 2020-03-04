from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    cSteps = 64
    while x:
        result = result << 1
        bit = x & 1
        result = result | bit 
        x = x >> 1
        cSteps -= 1
        # print(result)
    result = result << cSteps
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
