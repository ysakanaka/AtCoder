def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5+1)):
        if n%i==0:
            divisors.append(i)
            if i != n//i:
                divisors.append(n//i)

    return divisors

if __name__ == '__main__':
    N = int(input())
    divs = make_divisors(N)
    ans = 0
    for d in divs:
        if d == 1:
            continue
        if N%(d-1) == int(N/(d-1)):
            ans += d-1

    print(ans)
