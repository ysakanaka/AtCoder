from sys import stdin
N, M, C = (int(i) for i in input().split())
B = [int(x) for x in stdin.readline().rstrip().split()]
A = [[int(i) for i in input().split()] for i in range(N)]

score = 0
for i in range(N):
    total = 0
    for j in range(M):
        total = total + A[i][j]*B[j]
    total = total + C
    if total > 0:
        score += 1

print(score)
