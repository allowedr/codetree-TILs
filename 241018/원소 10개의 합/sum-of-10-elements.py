a = list(map(int, input().split()))
cnt = 0
for i in range(len(a)) :
    cnt += a[i]
print(cnt)