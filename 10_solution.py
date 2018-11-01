#!/bin/python3

import sys

# Find sum of all primes not greater than N for T number of test cases

def is_Prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def Sum_of_Primes(n):
    primes = []
    for i in range(2,n+1):
        if is_Prime(i):
            primes.append(i)
    return sum(primes)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(Sum_of_Primes(n))
