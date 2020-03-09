from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    i = len(A) - 1;
    while (i >= 0):
        A[i] += 1
        if A[i] <= 9:
            return A 
        else:
            A[i] = 0
            i -= 1
    # can use A.insert(0, 1)
    # but the trick can be to set leftmost as one and push 0 to array
    A[0] = 1
    A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
