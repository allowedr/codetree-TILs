n = int(input())
for i in range(n, 0, -1) :
    print(' '*(2*(n-i)),end='')
    for j in range(i) :
        print(i-j, end=' ')
    print()