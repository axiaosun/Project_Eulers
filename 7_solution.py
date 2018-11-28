#!/usr/bin/env python3

# Generate Nth prime number, given t number of cases.

import sys

def nth_prime_number(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(nth_prime_number(n))
