arr_cnt = [0 for _ in range(4)]
for i in range(3):
    arr = list(input().split())
    if arr[0] == 'Y' and int(arr[1]) >= 37 :
        arr_cnt[0] += 1
    elif arr[0] == 'N' and int(arr[1]) >= 37 :
        arr_cnt[1] += 1
    elif arr[0] == 'Y' and int(arr[1]) < 37 : 
        arr_cnt[2] += 1
    else :
        arr_cnt[3] += 1
    
print(*arr_cnt, end=' ')
if arr_cnt[0] >= 2 :
    print('E')