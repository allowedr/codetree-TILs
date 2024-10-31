arr = ["apple", "banana", "grape", "blueberry", "orange"]
c = input()
cnt = 0
for i in range(len(arr)):
    if arr[i][2] == c or arr[i][3] == c :
        print(arr[i])
        cnt += 1
print(cnt)