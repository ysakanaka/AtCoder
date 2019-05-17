from sys import stdin

def fun():
    n = (int(i) for i in input().split())

    l = [int(x) for x in stdin.readline().rstrip().split()]

    l = list(set(l))
    l.sort()

    while 1 < len(l):
        k = len(l)
        for i in range(1, k):
            if l[k-i]%l[0] == 0:
                l.pop(k-i)
            elif l[k-i] - l[k-i-1] == 1:
                print(1)
                return
            else:
                l[k-i] = l[k-i]%l[0]
        #l = [e for e in l if e != 0]
        l = list(set(l))
        l.sort()

        if l[0]==1:
            print(1)
            return

    print(l[0])
    return

if __name__ == '__main__':
    fun()
