from sys import stdin
import math

people = int(input())
sus = [int(input()) for i in range(5)]

minpeople = min(sus)

div = math.ceil(people/minpeople)

print(5+div-1)
