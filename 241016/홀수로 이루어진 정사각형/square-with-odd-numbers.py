n = int(input())
for i in range(1, n*2, 2) :
    for j in range(i, n*2+i) :
        if j % 2 != 0 :
            print(j+10, end=' ')
        else :
            print(end='')
    print()