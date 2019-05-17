import sys
from sys import stdin
sys.setrecursionlimit(2000000000)

def search(arg, target, l, diff):
    pos = arg.find(target)
    if pos == -1:
        return l
    l.append(diff+pos)
    if len(arg) > 0:
        return search(arg[pos+1:], target, l, diff+pos+1)
    else:
        return l


N, Q = [int(x) for x in stdin.readline().rstrip().split()]
s = input()
td = [[i for i in input().split()] for i in range(Q)]

count = 0
l = []
deleted = ""
for i in range(N):
    l.append([s[i], 1])

for t, d in td:

    poss = search(s, t, [], 0)
    #print(poss)
    for i in poss:
        if l[i][0] == t:
            if i==0 and d == "L":
                l[i][1] = 0
            elif i==N-1 and d == "R":
                l[i][1] = 0
            elif d == "L":
                l[i-1][1] += l[i][1]
                l[i][1] =0
            else:
                l[i+1][1] += l[i][1]
                l[i][1] =0
    #print(l)
count = 0
for e in l:
    count += e[1]
print(count)
