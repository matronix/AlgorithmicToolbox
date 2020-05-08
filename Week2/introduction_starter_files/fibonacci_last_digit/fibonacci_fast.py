# Uses python3
#from stress_test import *
from functools import lru_cache


#@timing_function
@lru_cache(1000)
def calc_fib_fast(n):
    if (n <= 1):
        return n

    return calc_fib_fast(n - 1) + calc_fib_fast(n - 2)


if __name__=='__main__':
    n = int(input())
    print(calc_fib_fast(n))
