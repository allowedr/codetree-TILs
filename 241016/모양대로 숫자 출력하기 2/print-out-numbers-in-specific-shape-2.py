n = int(input())
cnt = 1
for i in range(n):
    for j in range(n*2+1):
        cnt += 1
        if cnt >= 10 :
            cnt = 1
        if cnt % 2 == 0 :
            print(cnt, end=' ')
        else :
            print(end='')
        
    print()