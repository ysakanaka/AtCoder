from sys import stdin
cases = int(input())

for i in range(cases):
    R, C = [int(x) for x in stdin.readline().rstrip().split()]
    Office = [[int(i) for i in input().split()] for i in range(R)]
    Dist = [[0 for i in range(C)] for j in range(R)]

    for j in range(R):
        for k in range(C):
            if Office[j][k] == 1:
                Dist[j][k] == 0
            else:
                min = 250*250
                for l in range(R):
                    for m in range(C):
                        distance = abs(j-l)+ abs(k-m)
                        if distance < min:
                            min = distance
                Dist[j][k] = min
