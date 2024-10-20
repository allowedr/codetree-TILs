arr = list(map(int, input().split()))
s = 0
for i in range(len(arr)):
    if arr[i] == 0 :
        s += arr[i-1]
        s += arr[i-2]
        s += arr[i-3]
        break
print(s)