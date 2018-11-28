#!/usr/bin/env python3

import sys


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()

    str_ = str(num)
    lst_ = []
    for digit in str_:
        lst_.append(int(digit))

    products = []
    for i in range(0,n-k+1):
        p = 1
        for x in lst_[i:(i+k)]:
            p *= x
        products.append(p)

    print (max(products))
