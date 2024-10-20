arr = list(map(int, input().split()))
cnt = 0
s = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0 and arr[i] != 0 and arr[i] != 1:
        cnt += 1
        s += arr[i]
print(cnt, s)