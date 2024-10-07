c, n = input().split()
if c == 'A' :
    for i in range(1, n) :
        print(i, end=' ')
elif c == 'D' :
    for j in range(n, 0, -1) :
        print(j, end=' ')