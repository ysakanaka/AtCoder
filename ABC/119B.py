from sys import stdin

def fun():
    n = int(input())
    total = 0

    for i in range(n):
        x, u = input().split()
        x = float(x)
        if u == 'JPY':
            total = total + x
        else:
            total = total + x*380000.0
    print(total)


if __name__ == '__main__':
    fun()
