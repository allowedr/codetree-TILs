c, n = input().split()
if c == 'A' :
    for i in range(1, int(n)+1) :
        print(i, end=' ')
elif c == 'D' :
    for j in range(int(n), 0, -1) :
        print(j, end=' ')