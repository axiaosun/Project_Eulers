#!/usr/bin/env python3

import math

def num_divisors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors +=2
        else:
            continue
    return number_of_factors

def find_tri_index(factor_limit):
    for n in range(1,1000000):
        Tn=(n*(n+1))/2
        if num_divisors(Tn) > factor_limit:
            return int(Tn)
         
t = int(input().strip())
for _ in range(t):
    n = int(input())
    print(find_tri_index(n))
