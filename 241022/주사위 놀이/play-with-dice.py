arr = list(map(int, input().split()))
cnt_arr = [0 for _ in range(6)]
for i in range(len(arr)):
    cnt_arr[arr[i]-1] += 1

for i in range(len(cnt_arr)):
    print(f'{i+1} - {cnt_arr[i]}')