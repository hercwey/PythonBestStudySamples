#!/usr/bin/env python
# -*-coding: utf-8-*-
'''
分数相加
'''

# 返回最大公约数
def gcd(a, b):
    if not a > b:
        a, b = b, a
    while b != 0:
        remainder = a % b
        a, b = b, remainder
    return a

#返回最小公倍数
def lcm(a, b):
    return (a * b) / gcd(a,b)

class Fraction(object):
    def __init__(self, number, denom=1):
        self.number = number
        self.denom = denom

    def __str__(self):
        return str(self.number) + '/' + str(self.denom)

    __repr__ = __str__

    def __add__(self, other):
        lcm_num = lcm(self.denom, other.denom)
        number_sum = (lcm_num / self.denom * self.number) + (lcm_num / other.denom * other.number)
        return Fraction(number_sum, lcm_num)

if __name__ == "__main__":
    m = Fraction(1,4)
    n = Fraction(1,6)
    s = m + n
    print m,"+",n,"=",s
    
