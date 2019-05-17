import itertools

N = int(input())
V = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

max = 0
pattern = itertools.product(range(2), repeat=N)
for p in pattern:
    sum = 0
    count = 0
    for i in p:
        if i == 1:
            sum += V[count]-C[count]
        else:
            pass
        count +=1
    if sum > max:
        max = sum


print(max)
