import sys

#Find the largest palindrome made from the product of two 3-digit numbers which is less than N

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def largest_pali(n):
    max_num = 0
    for i in range(999, 99, -1):
        for j in range(999, i-1, -1):
            x = i* j
            if x > n:
                continue
            if x <= max_num:
                break
            if isPalindrome(x)and x in range(max_num, n):
                max_num = x
    return max_num

t = int(input().strip())
for _ in range(t):
    n = int(input())
    print(largest_pali(n))
