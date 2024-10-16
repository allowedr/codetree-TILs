n = int(input())
cnt = 1
for i in range(n): 
    for j in range(n):
        if i % 2 == 0 :
            print(cnt, end=' ')
        else :
            print(cnt+n-1-(j*2), end=' ')
        cnt += 1
    print()