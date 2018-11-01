#!/usr/bin/env python3

# Sum of even fibonacci numbers sequence
# Given t number of test cases, find the sum of even-valued numbers in a Fibonacci sequence where the sequence's values do not exceed n

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    n1, n2, total = 0,2,0
    
    while n2 <= n:
        total += n2
        n1, n2 = n2, n1+4*n2
    
    print(total)
