# Uses python3
import sys

def gcd_fast(a, b):
    if b == 0:
        return a
    a_prime = a%b
    return gcd_fast(b,a_prime)


if __name__ == "__main__":
    #input = sys.stdin.read()
    input = input()
    a, b = map(int, input.split())
    print(gcd_fast(a, b))
