import itertools

N = int(input())
V = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

sum = 0
for i in range(N):
    if V[i]-C[i] > 0:
        sum += V[i]-C[i]

print(sum)
