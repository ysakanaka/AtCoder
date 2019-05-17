from sys import stdin

N= int(input())
l = input()

if l.count("B") < l.count("R"):
    print("Yes")
else:
    print("No")
