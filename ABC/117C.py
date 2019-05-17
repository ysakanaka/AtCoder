import sys
N, M = (int(i) for i in input().split())
X = [int(i) for i in input().split()]
X.sort()

pos = [[0] * 2 for i in range(N)]
total = 0

if M <= N:
    print(0)
    sys.exit()

for i in range(N):
    pos[i][0] = i
    pos[i][1] = abs(X[i+1] - X[i])
    total = total + pos[i][1]

pos = sorted(pos, key=lambda x:(x[1]))

for j in range(N, M-1):
    dim = abs(X[j+1]-X[j])
    total = total + dim
    if pos[0][1] < dim:
        pos[0][0] = j
        pos[0][1] = dim
        pos = sorted(pos, key=lambda x:(x[1]))


for i in range(1, N):
    total = total - pos[i][1]

print(total)
