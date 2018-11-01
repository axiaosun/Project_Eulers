#!/bin/python3

import sys

# Given t test cases, find the largest prime factor of given number n.

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    i = 2
    largest_prime = 2
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n = n // i
        i += 1
    if n > largest_prime:
        largest_prime = n
    print(largest_prime)
