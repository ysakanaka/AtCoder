from sys import stdin

n, m = (int(i) for i in input().split())

l = [int(x) for x in stdin.readline().rstrip().split()]
l.pop(0)
for i in range(n-1):
    l2 = [int(x) for x in stdin.readline().rstrip().split()]
    l2.pop(0)
    l = list(set(l)&set(l2))

print(len(l))
