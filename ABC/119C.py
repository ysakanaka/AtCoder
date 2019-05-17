from sys import stdin

def fun(mp, abc, l):
    abs_abc = [[1000000, 0], [10000000, 0], [1000000, 0]]

    for i in range(n):
        for j in range(3):
            if abs(l[i]-abc[j]) < abs_abc[j][0]:
                abs_abc[j][0] = abs(l[i]-abc[j])
                abs_abc[j][1] = i

    for k in range(1, 4):
        if abs_abc[3-k][0] == 0:
            abc.pop[3-k]
            abs_abc.pop(3-k)
            l.pop(abs_abc[3-k][1])
        elif abs_abc[3-k][0] < 11:
            mp += abs_abc[3-k]
            l.pop(abs_abc[3-k][1])
            abs_abc.pop(3-k)

    if len(abc) == 0:
        print(mp)
        return

    for p in range(ren(l)):
        for q in range(p+1, ren(l)) :
            for r in range(len(abc)):
                if abs(abc[r]-(l[p]+l[q])) < abs_abc[r]:

def search(abc, l, abs_abc):
    for i in range(1, len(l)):
        for j in range(i+1, len(l)+1):
            for r in range(len(abc)):
                if abs(abc[r]-(l[len(l)-i]+l[len(l)-j])) < abs_abc[r]:
                    l[len(l)-i] = l[len(l)-i]+l[len(l)-j]
                    l.pop(len(l)-j)
                    abs_abc[r] = abs(abc[r]-(l[len(l)-i]+l[len(l)-j]))

if __name__ == '__main__':
    mp = 0
    n, a, b, c = (int(i) for i in input().split())
    abc = [a, b, c]
    l = [int(input()) for i in range(n)]
    fun(mp, abc, l)
