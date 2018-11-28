#!/usr/bin/env python3

# Given N, Check if there exists any Pythagorean triplet for which a+b+c = N, for t number of cases.
# Find maximum possible value of the product of abc among all such Pythagorean triplets. If there is no such Pythagorean triplet print -1.

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    lst_ = [-1]
    for a in range(3, int(n/3)):
        for c in range(int(n/3), int(n/2)):
            b = n - a - c
            if a**2 + b**2 == c**2:
                lst_.append(a*b*c)
    print(max(lst_))
