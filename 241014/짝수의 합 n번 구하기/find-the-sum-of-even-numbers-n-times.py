n = int(input())
for i in range(n) :
    c = 0
    a, b = map(int, input().split())
    for j in range(a, b+1) :
        if j % 2 == 0 :
            c += j
    print(c)