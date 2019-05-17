from sys import stdin
R, G, B, N = (int(i) for i in input().split())

dp = [0] * (N+1)
dp[0] = 1

for c in (R, G, B):
    for i in range(N + 1):
        if i + c <= N:
            dp[i+c] += dp[i]

print(dp[N])
