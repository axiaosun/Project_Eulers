#!/usr/bin/env python3

#Work out the first ten digits of the sum of N 50-digit numbers.

n = int(input().strip())
sums = []
for _ in range(n):
    lst_ = [int(i) for i in input().strip().split(' ')]
    sums.append(sum(lst_))

sums = sum(sums)

print(int(str(sums)[:10]))
