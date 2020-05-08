# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
#print(type(a))
assert(len(a) == n)

"""result = 0

for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]
"""

max1 = max(a)
#print("The max element of the list is %s\n" % (max1))
a.remove(max1)
#print("The modified list is %s" % (a))
max2 = max(a)
#print("The second max element of the list is %s\n" % (max2))
result = max1*max2
print(result)
