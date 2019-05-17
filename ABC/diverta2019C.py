from sys import stdin
N = int(input())

middle = 0
countB = 0
countA = 0
countBA = 0
sumcount = 0

for i in range(N):
    s = input()
    middle += s.count("AB")
    if s[0] == "B" and s[-1] == "A":
        countBA +=1
    elif s[0] == "B":
        countB +=1
    elif s[-1] == "A":
        countA +=1
if countBA > 0:
    sumcount += countBA -1
    if countA > 0:
        sumcount +=1
        countA -= 1
    if countB > 0:
        sumcount +=1
        countB -= 1

t = min(countA, countB)

print(sumcount+middle+t)
