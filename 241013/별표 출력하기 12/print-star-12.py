n = int(input())
for i in range(n, -1, -1) :
    for j in range(i) :
        if i == n :
            print('* '*i, end='')
        if i % 2 == 0 :
            print('* ', end='')
        else :
            print(' ', end='')
    print()