s = input()
arr = list(s)

for i in range(len(arr)):
    if arr[i] == arr[1] :
        arr[i] = arr[0] :
s = ''.join(arr)
print(s)