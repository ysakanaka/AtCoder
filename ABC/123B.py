from sys import stdin
import itertools
#print('permutations(range(4))   : ', list(itertools.permutations(range(4) ) ) )

foods = [int(input()) for i in range(5)]
orders = list(itertools.permutations(range(5)))
mintime = 1111111111
ordertime = 0
nowtime = 0
for i in orders:
    ordertime = 0
    l = list(i)
    #print(l)
    ordertime += foods[l[0]]
    for j in range(1, 5):
        #print(ordertime)
        if ordertime%10 == 0:
            ordertime+= foods[l[j]]
        else:
            while ordertime%10 !=0:
                ordertime += 1
            ordertime+=foods[l[j]]
    if mintime > ordertime:
        mintime = ordertime

print(mintime)
