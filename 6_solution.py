#!/usr/bin/env python3

#Find the absolute difference between the sum of the squares of the first N natural numbers and the square of the sum, given t number of inputs.

import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())

    sum_of_squares = sum([i**2 for i in range(1,n+1)])
    square_of_sum = (sum([i for i in range(1,n+1)]))**2

    print(abs(sum_of_squares - square_of_sum))
