s = input()
f = s[0]
c = s[1]

arr = list(s)
arr[0], arr[1] = arr[1], arr[0]
for i in range(2, len(arr)):
    if arr[i] == arr[1] :
        arr[i] = arr[0]
    elif arr[i] == arr[0] :
        arr[i] = arr[1]


s = ''.join(arr)

print(s)