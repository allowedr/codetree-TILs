arr = list(map(int, input().split()))
for i in range(len(arr)):
    if arr[i] == 0 :
        for j in range(arr.index(arr[i])-1, -1, -1):
            print(arr[j], end=' ') 
        break
        for j in range(len(arr), -1, -1):
           print(arr[j], end=' ')