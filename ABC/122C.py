from sys import stdin
import re
N, Q = (int(i) for i in input().split())
s = input()
lr = [[int(i) for i in input().split()] for i in range(Q)]
ms = re.finditer("AC", s)
ml = list(ms)
for i in range(Q):
    count = 0
    for j in range(len(ml)):
        a, b = ml[j].span()
        #print(a, b)
        #print("q", lr[i])
        if lr[i][0]-1 <= a and b <= lr[i][1]:
            count = count +1
            #print("counted")
        if lr[i][1] < a:
            break

    print(count)
