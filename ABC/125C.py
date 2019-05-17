from functools import reduce
import numpy as np

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_list(numbers):
    return reduce(gcd, numbers)

N = int(input())
A = [int(i) for i in input().split()]
cur = 0
max = gcd_list(A[1:N])

for i in range(N):
    cur = gcd_list(A[0:i]+A[i+1:N])
    if cur != max:
        break

print(cur)
