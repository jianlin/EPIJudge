import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


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

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # TODO - you fill in here.

    the_pivot = A[pivot_index]
    print("PIVOT", A[pivot_index])
    print ("NOW0", A, the_pivot)
    pOdd = 0
    pEven = len(A) - 1
    while pOdd < pEven:   # if equal, that's ok, the number can be even or odd and it is fine
        if A[pOdd] < the_pivot:
            pOdd += 1
        elif A[pEven] >= the_pivot:
            pEven -= 1
        else:    # now we are ready to do a swap
            A[pOdd], A[pEven] = A[pEven], A[pOdd]
            pOdd += 1
            pEven -= 1

    print ("NOW First Pass", A)
    pOdd = 0
    while pOdd < len(A) and A[pOdd] < the_pivot:
        pOdd += 1

    print ("NOW2", pOdd, the_pivot, A[pOdd], A[pOdd -1])              
    # now pOdd is at the "greater than or eq region"        

    # TODO pass function in Python and make it just a helper function
    pEven = len(A) - 1
    while pOdd < pEven:   # if equal, that's ok, the number can be even or odd and it is fine
        print ("INDEX", pOdd, pEven, A[pOdd], A[pEven])
        if A[pOdd] == the_pivot:
            pOdd += 1
        elif A[pEven] != the_pivot:
            pEven -= 1
        else:    # now we are ready to do a swap
            A[pOdd], A[pEven] = A[pEven], A[pOdd]
            pOdd += 1
            pEven -= 1
    print ("NOW2", A)   
    # print ("NOW3")       
    # pOdd = 0
    # while pOdd < len(A):
    #     print (pOdd, A[pOdd])
    #     pOdd += 1
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
