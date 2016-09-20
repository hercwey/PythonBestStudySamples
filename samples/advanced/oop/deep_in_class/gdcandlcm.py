#!/usr/bin/env python

def gcd(a, b):
    if not a > b:
        a, b = b, a
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    return a

def lcm(a, b):
    return (a * b) / gcd(a,b)

if __name__ == "__main__":
    print gcd(8, 20)
    print lcm(8, 20)
