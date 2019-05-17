from sys import stdin

N, Q = [int(x) for x in stdin.readline().rstrip().split()]
s = input()
td = [[i for i in input().split()] for i in range(Q)]

count = 0
dict = {}
deleted = ""
for i in range(N):
    if s[i] in dict:
        dict[s[i]].append(i+1)
    else:
        dict[s[i]] = [i+1]
print(dict)
for t, d in td:
    if t not in dict:
        continue
    if d == "L":
        dict[t] = map(lambda x: x-1, dict[t])
    else:
        dict[t] = map(lambda x: x-1, dict[t])

    dict[t]= [i for i in dict[t] if not i == 0]
    dict[t]= [i for i in dict[t] if not i == N+1]
    print(dict)

count = 0
for e in dict.values():
    count += len(e)

print(count)
