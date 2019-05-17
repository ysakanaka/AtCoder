from sys import stdin
N, M = (int(i) for i in input().split())
AB = [[int(i) for i in input().split()] for i in range(N)]

AB = sorted(AB)
#total = 0
money = 0
for i in range(N):
    m = min(AB[i][1], M)
    money += AB[i][0]*m
    M = M - m
    if M == 0:
        break

print(money)
