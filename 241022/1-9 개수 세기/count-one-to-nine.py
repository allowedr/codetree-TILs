n = int(input())
arr = list(map(int, input().split()))
cnt_arr = [0 for _ in range(9)]
for i in range(n):
    cnt_arr[arr[i]-1] += 1

for i in range(len(cnt_arr)):
    print(cnt_arr[i])