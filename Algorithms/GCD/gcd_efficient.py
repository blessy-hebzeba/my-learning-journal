# Uses python3
import sys


def gcd_efficient(m, n):
    a = max(m, n)
    b = min(m, n)
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a


if __name__ == "__main__":
    inputs = input()
    p, q = map(int, inputs.split())
    print(gcd_efficient(p, q))
