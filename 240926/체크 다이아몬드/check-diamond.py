n = int(input())
for i in range(1, n+1) :
    print(' ' * (n-i), end = '')
    print('* '*i, end= '')
    print()
    if i >= n :
        for j in range(n-1, 0, -1) :
            print(' ' * (n-j), end = '')
            print('* '*j, end= '')
            print()