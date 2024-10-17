n = int(input())
cnt = 1
for i in range(n, 0, -1):
    print(' '*2*(n-i), end='')
    for j in range(i):
        print(cnt, end=' ')
        cnt += 1
        if cnt >= 10 :
            cnt = 1
    print()