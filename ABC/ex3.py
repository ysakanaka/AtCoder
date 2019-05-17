from sys import stdin

N, Q = [int(x) for x in stdin.readline().rstrip().split()]
s = input()
td = [[i for i in input().split()] for i in range(Q)]

count = 0
dict = {}
deleted = ""
for i in range(N):
    dict[s[i]] = i+1

for t, d in td:
    if
    if d == "L":
        dict[t] -= 1
    else:
        dict[t] +=1

    if dict[t] == 0 or dict[t] == N+1:
        dict[t] == "deleted"


print(N-count)
