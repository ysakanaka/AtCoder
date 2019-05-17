from sys import stdin
R, G, B, N = (int(i) for i in input().split())

count = 0
for i in range(N+1):
    N1 = N - i*R
    for j in range(N1+1):
        b = (N1 - j*G)/B
        if b.is_integer() and b >= 0:
            count +=1

print(count)
