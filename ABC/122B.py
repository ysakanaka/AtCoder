from sys import stdin
s = input()
a = []
a.append(s.find('A'))
a.append(s.find('T'))
a.append(s.find('G'))
a.append(s.find('C'))
for i in range(len(a)):
    if a[i] == -1:
        a[i] = 100
start = min(a)
#print(a)
pos = 0
sol = 0
for i in range(start, len(s)):
    #print(start)
    if s[i] != 'A' and s[i]!='T' and s[i]!='G' and s[i]!='C':
        pos = i
        if pos - start > sol:
            sol = pos - start
        #start = i+1
        a.clear()
        a.append(s.find('A', i))
        a.append(s.find('T', i))
        a.append(s.find('G', i))
        a.append(s.find('C', i))
        for i in range(len(a)):
            if a[i] == -1:
                a[i] = 100
        start = min(a)
if len(s)- start > sol:
    sol = len(s)-start
print(sol)
