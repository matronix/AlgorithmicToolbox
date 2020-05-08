# Uses python3

import random
import time

def timing_function(some_function):
    """
        Outputs the time a function takes
        to execute.
    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        some_function(*args, **kwargs)
        t2 = time.time()
        print ('%r %5.2f ms' % (some_function.__name__, (t2-t1)*1e3))
    return wrapper


@timing_function
def max_product(a):
    result = 0

    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result


@timing_function
def max_product_fast(a):
    result = 0
    max1 = max(a)
    a.remove(max1)
    max2 = max(a)
    result = max1*max2
    return result


if __name__ == '__main__':
    #n = int(input())
    #a = [int(x) for x in input().split()]
    while(True):
        n = random.randint(2,20000)
        a=[random.randint(0,10000) for x in range(n)]
        assert(len(a) == n)
        result1 = max_product(a)
        result2 = max_product_fast(a)

        if(result1==result2):
            print('OK')
        else:
            print('Wrong: Result1 is %i, Result2 is %i\n' % (result1,result2))

