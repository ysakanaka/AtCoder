from sys import stdin

def fun():
    a, b, q = (int(i) for i in input().split())
    pre_st = [int(input()) for i in range(a)]
    st = [[]]
    for ut in range(a+b):
        st[ut][0] = pre_st[ut]
        if ut < a:
            st[ut][1] = 0 #a
        else:
            st[ut][1] = 1 #b

    st = sorted(st)
    x = [int(input()) for i in range(q)]


    for i in range(q):
        pos = 0
        total1 = None
        total2 = None
        for j in range(a+b):
            if x[i] < st[j][0]:
                pos = j
                break
        for k in range(pos+1, a+b):
            if st[k][1] != st[pos][1]:
                total1 = (st[pos][0]-x[i])+(st[k][0]-x[i])


        for e in range(a+b+1):
            if x[i] < st[a+b-e][0]:
                pos = a+b-e
                break
        for f in range(pos+1, a+b+1):
            if st[a+b-f][1] != st[pos][1]:
                total2 = (x[i]-st[pos][0])+(x[i]-st[a+b-f][0])

        for o in range(a+b+1):
            if x[i] < st[a+b-e][0]:
                pos = a+b-e
                break
        for d in range(pos+1, a+b+1):
            if st[a+b-f][1] != st[pos][1]:
                total2 = (x[i]-st[pos][0])+(x[i]-st[a+b-f][0])


if __name__ == '__main__':
    fun()
