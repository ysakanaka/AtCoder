a, b, c = (int(i) for i in input().split())

count = 0
for i in range(c):
    if b >= a:
        b = b-a
        count = i+1
    i+=1

print(count)
