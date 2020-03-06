from test_framework import generic_test

def parity(x: int) -> int:
    p = 0
    while x:
        p = ~p
        x = x & (x-1)
<<<<<<< HEAD
    return p & 1 
=======
    p = 0
    return p & 1
>>>>>>> d1a03d19726d39edcf9b708ef0336114ed5322f1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
