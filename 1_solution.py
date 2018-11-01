#!/usr/bin/python3

import sys

# Find sum of all multiples of 3 and 5 below N

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = ((n-1)//3)
    b = ((n-1)//5)
    c = ((n-1)//15)
    sum = (((3*a*(a+1))//2)+((5*b*(b+1))//2)-((15*c*(c+1))//2))
    print(int(sum))
