N = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if arr[i] == min(arr) :
        cnt += 1
print(min(arr), cnt)