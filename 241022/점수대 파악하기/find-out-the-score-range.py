arr = list(map(int, input().split()))
cnt_arr = [0 for _ in range(10)]
num = -10
for i in range(len(arr)):
    if arr[i] == 0 :
        break
    cnt_arr[(arr[i]//10)-1] += 1


for i in range(len(cnt_arr)-1, -1, -1):
    print(f'{-(num-(i*10))} - {cnt_arr[i]}')