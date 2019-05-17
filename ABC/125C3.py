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
max = gcd_list(A)

for i in range(1, N):
    if max < gcd_list(A[i:N]):
        A[i] = A[i-1]

print(gcd_list(A))
