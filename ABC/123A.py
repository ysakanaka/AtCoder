from sys import stdin

def solve(a, k):
    count = 0
    for i in range(5):
        for j in range(5):
            if i == j:
                continue
            elif abs(a[i]-a[j]) > k:
                return ":("
    return "Yay!"


if __name__ == '__main__':
    antena = [int(input()) for i in range(5)]
    k = int(input())
    print(solve(antena, k))
