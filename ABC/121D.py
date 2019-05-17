A, B = (int(i) for i in input().split())

total = A
for i in range(A+1, B+1):
    #print("i", i)
    #print("total", total)
    total = total^i


print(total)
