n = int(input())
for i in range(1, n+1) :
    tmp = 0
    for j in range(1, i+1) :
        if i % j == 0 :
            tmp += 1
    if tmp == 2 :
        print(i, end = ' ')