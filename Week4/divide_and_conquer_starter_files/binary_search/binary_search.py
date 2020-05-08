# Uses python3
import sys
import math
import time

"""
def timing_function(some_function):
        Outputs the time a function takes
        to execute.
    def wrapper(*args, **kwargs):
        print('args:{}\n'.format(args))
        t1 = time.time()
        some_function(*args, **kwargs)
        t2 = time.time()
        #print ('%r %5.2f ms' % (some_function.__name__, (t2-t1)*1e3))
        return '{} {:05.2f}\n'.format(some_function.__name__, (t2-t1)*1e3)
        #print('{} {:05.2f}\n'.format(some_function.__name__, (t2-t1)*1e3))
        #return some_function
    return wrapper
"""

#@timing_function
def binary_search(a, x):
    left, right = 0, len(a)-1
    #a.sort()
    return BinarySearch(a, left, right, x)

def BinarySearch(a, low, high, key):
    if high < low:
        return -1
    mid = math.floor(low + (high-low)/2.0)
    if key == a[mid]:
        return mid 

    if key < a[mid]:
        return BinarySearch(a, low, mid-1, key)
    else:
        return BinarySearch(a, mid+1, high, key)


#@timing_function
def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(linear_search(a, x), end=' ')
        print(binary_search(a, x), end=' ')
    #print('\n')
