#Uses python3
import sys
import math


def get_majority_element(a, left, right):
    #print("a:{}".format(a.__str__()))
    #print("left:{}".format(left))
    #print("right:{}".format(right))
    if right<0:
        return -1
    if left == right:
        return a[left] 
    if left + 1 == right and a[left]==a[right]:
        return a[left]
    #the mid index
    mid = math.floor(left + (right-left)/2.0)
    #print("mid:{}".format(mid))
    ml = get_majority_element(a[left:mid+1], left, mid)
    #print("ml:{}".format(ml))
    mr = get_majority_element(a[mid+1:], 0, len(a[mid+1:])-1)
    #print("mr:{}".format(mr))
    #print("a:{}".format(a.__str__()))
    if a.count(mr) > len(a)/2.0:
        return mr
    elif a.count(ml) > len(a)/2.0: 
        return ml
    else:
        return -1

    return -1

"""
B and C are sorted arrays,
"""
def merge_sorted(B, C):
    #find size_B + size_C
    size_B = len(B)
    size_C = len(C)
    D=[]
    #Compare the first elements of the sorted arrays B & C
    #Remove the smaller one and append to D
    while len(B)!=0 and len(C)!=0:
        b=B[0]
        c=C[0]
        if b<=c:
            D.append(b)
            B.remove(b)
        else:
            D.append(c)
            C.remove(c)

    #check the remainig arrays B and C. The one that  is non zero 
    #lenght is appended to end of D
    if len(B)!=0:
        for i in B:
            D.append(i)
    if len(C)!=0:
        for i in C:
            D.append(i)

    return D



if __name__ == '__main__':
    #print("I am in {}".format(__name__))
    #input = sys.stdin.readline()
    input = sys.stdin.read()
    #input = input()
    n, *a = list(map(int, input.split()))
    #a.sort()
    n=n-1
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
