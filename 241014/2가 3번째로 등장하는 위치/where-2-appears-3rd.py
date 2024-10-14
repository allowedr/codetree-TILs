n = int(input())
cnt = 0
a = list(map(int, input().split()))
for i in range(len(a)) :
    if a[i] == 2 :
        cnt += 1
        if cnt == 3 :
            print(i+1)
            break