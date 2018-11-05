#!/bin/python3

import sys
import functools

# What is the smallest positive number that is evenly divisible(divisible with no remainder) by all of the numbers from to N?

def gcd_(a,b):
    # Return greatest common divisor using Euclid's algo
    while b != 0:
        a,b = b,a%b
    return a

def lcm_(a,b):
    # Return lowest common multiple
    return a*b//(gcd_(a,b))

def smallest_cm(*args):
    # Reduce lcm of args
    return functools.reduce(lcm_, args)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(smallest_cm(*range(1,n+1)))

