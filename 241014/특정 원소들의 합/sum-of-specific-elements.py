a=[]
b=0
for _ in range(4) :
    a.append(list(map(int, input().split())))
for i in range(4) :
    for j in range(i+1) :
        b += a[i][j]
print(b)