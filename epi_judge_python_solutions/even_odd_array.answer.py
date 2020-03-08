import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# This is the Chapter 5 intro problem

def even_odd(A: List[int]) -> None:
    pOdd = 0
    pEven = len(A) - 1
    while pOdd < pEven:   # if equal, that's ok, the number can be even or odd and it is fine
        if A[pOdd] % 2 == 0:
            pOdd += 1
        elif A[pEven] % 2 != 0:
            pEven -= 1
        else:    # now we are ready to do a swap
            A[pOdd], A[pEven] = A[pEven], A[pOdd]
            pOdd += 1
            pEven -= 1
    return A

    # next_even, next_odd = 0, len(A) - 1
    # while next_even < next_odd:
    #     if A[next_even] % 2 == 0:
    #         next_even += 1
    #     else:
    #         A[next_even], A[next_odd] = A[next_odd], A[next_even]
    #         next_odd -= 1


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
