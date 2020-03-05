from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    # print(x)
    if x == 0:
        return True
    elif x < 0:
        return False
    xTmp = x
    rev = 0
    while (x != 0):
        rev *= 10
        last = x - ( x // 10 ) * 10
        rev = rev + last
        x = x // 10
        # invariant: at this point, x loses 1 digit at right, and that digit went to the right of rev, which is pushed left if x has more digits (non zero)
    return xTmp == rev

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
