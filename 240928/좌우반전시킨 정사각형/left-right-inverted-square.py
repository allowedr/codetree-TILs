n = int(input())
a = 1

for i in range(1, n+1) :
    for j in range(n, 0, -1) :
        print(i * j, end=' ')
    print()