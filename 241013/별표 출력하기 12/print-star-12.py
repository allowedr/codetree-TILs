n = int(input())
for i in range(n, -1, -1) :
    for j in range(i) :
        if j % 2 == 0:
            print('* '*i, end='')