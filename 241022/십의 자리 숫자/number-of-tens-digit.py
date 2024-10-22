arr = list(map(int, input().split()))
cnt_arr = [0 for _ in range(9)]

for i in range(len(arr)):
    if arr[i]//10 != 0:
        cnt_arr[(arr[i]//10)-1] += 1
    if arr[i] == 0 :
        break
    
for i in range(len(cnt_arr)):
    print(f'{i+1} - {cnt_arr[i]}')