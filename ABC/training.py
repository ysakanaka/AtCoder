from sys import stdin
cases = int(input())

for i in range(cases):
    N, P = [int(x) for x in stdin.readline().rstrip().split()]
    skills = [int(x) for x in stdin.readline().rstrip().split()]

    a = sum(skills)/len(skills)
    while P < len(skills):
        for i in range(len(skills)):
            
