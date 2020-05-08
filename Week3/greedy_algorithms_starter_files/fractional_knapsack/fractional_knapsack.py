# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    vperw = [values[n]/weights[n] for n in range(0,len(values))]
    d={}
    for i in range(0,len(weights)):
        d[vperw[i]]=weights[i]
    #print(*vperw)
    vperw.sort()
    vperw.reverse()
    #print(d)
    for i in range(0,len(vperw)):
        if capacity==0:
            return value
        a = min(d[vperw[i]],capacity)
        #print('a:%i\n' % (a))
        #value = value + a*d[weights[i]]
        value = value + a*vperw[i]
        #print('value:%f\n' % (value))
        capacity = capacity - a
        #print('capacity:%f\n' % (capacity))
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    #print("values: ")
    #print(*values)
    #print("\n")
    weights = data[3:(2 * n + 2):2]
    #print("weights: ")
    #print(*weights)
    #print("\n")
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
