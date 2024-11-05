arr = list(map(int, input().split()))

for i in range(len(arr)):
    arr[i] = chr(arr[i])
print(*arr)