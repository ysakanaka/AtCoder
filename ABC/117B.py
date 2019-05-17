N = int(input())
L = [int(i) for i in input().split()]

m = max(L)
if m < sum(L)-m:
    print('Yes')
else:
    print('No')
