# Uses python3
#from stress_test import *
from functools import lru_cache


#@timing_function
@lru_cache(1000)
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)



n = int(input())
print(calc_fib(n))
