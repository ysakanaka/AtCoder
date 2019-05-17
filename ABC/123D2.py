from sys import stdin

X, Y, Z, K = (int(i) for i in input().split())
A = [int(x) for x in stdin.readline().rstrip().split()]
B = [int(x) for x in stdin.readline().rstrip().split()]
C = [int(x) for x in stdin.readline().rstrip().split()]

yammy = []
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

a = 0
b = 0
c = 0

print(A[0]+B[0]+C[0])
div = [0, 1, 2]
div2 = [0, 1]
div3 = []

for i in range(1, K):
    #print(div)
    #print(A)
    if a < Z-1 and b < Y-1 and c < Z-1:
        div[0] = (A[a]-A[a+1])
        div[1] = (B[b]-B[b+1])
        div[2] = (C[c]-C[c+1])
        minid = div.index(min(div))
        if minid == 0:
            a+=1
        elif minid == 1:
            b +=1
        else:
            c+=1
    elif b < Y-1 and c < Z-1:
        div2[0] = (B[b]-B[b+1])
        div2[1] = (C[c]-C[c+1])
        minid = div.index(min(div2))
        if minid == 0:
            b +=1
        else:
            c+=1
    elif a < X-1 and c < Z-1:
        div2[0] = (A[a]-A[a+1])
        div2[1] = (C[c]-C[c+1])
        minid = div.index(min(div2))
        if minid == 0:
            a +=1
        else:
            c+=1
    elif a < X-1 and b < Y-1:
        div2[0] = (A[a]-A[a+1])
        div2[1] = (B[b]-B[b+1])
        minid = div.index(min(div2))
        if minid == 0:
            a +=1
        else:
            b+=1
    elif a < X-1:
        a+=1
    elif b < Y-1:
        b+=1
    elif c < Z-1:
        c+=1
    else:
        break

    print(A[a]+B[b]+C[c])
