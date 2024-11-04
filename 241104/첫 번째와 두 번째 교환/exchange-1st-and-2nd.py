s = input()
arr = list(s)

f = arr[0]
c = arr[1]

for i in range(1, len(arr)):
    if arr[i] == f :
        arr[i] = c

arr[0], arr[1] = arr[1], arr[0]

s = ''.join(arr)

print(s)