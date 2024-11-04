s = input()
f = s[0]
c = s[1]

arr = list(s)

for i in range(len(arr)):
    if arr[i] == c :
        arr[i] = f

arr[0], arr[1] = arr[1], arr[0]

s = ''.join(arr)

print(s)