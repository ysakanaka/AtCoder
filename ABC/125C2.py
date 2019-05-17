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
count = 1

while True:
    count+=1
    for i in range(N):
        if A[i]%count == 0:
            pass
        else:
            A[i] = A[i-1]
            break
    else:
        continue
    break

print(gcd_list(A))
