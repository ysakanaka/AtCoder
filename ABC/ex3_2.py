from sys import stdin

N, Q = [int(x) for x in stdin.readline().rstrip().split()]
s = input()
td = [[i for i in input().split()] for i in range(Q)]

count = 0
l = []
deleted = ""
for i in range(N):
    l.append([s[i], i+1])

for t, d in td:
    r = len(l)
    for i in range(1, r+1):
        if l[r-i][0] == t:
            if d == "L":
                l[r-i][1] -= 1
            else:
                l[r-i][1] += 1

            #print(l[r-i][1])
            if l[r-i][1] == 0 or l[r-i][1] == N:
                l.pop(r-i)
    print(l)

print(len(l))
