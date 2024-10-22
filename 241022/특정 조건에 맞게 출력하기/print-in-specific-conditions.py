arr = list(map(int, input().split()))
n = len(arr)
for i in range(n) :
    if arr[i] == 0 :
        break
    if arr[i] % 2 == 0 and arr[i] != 1 :
        print(arr[i]//2, end=' ')
    else :
        print(arr[i]+3, end=' ')