n = int(input())
arr = []
length = 0
cnt = 0

for _ in range(n):
    arr.append(input())
for i in range(n):
    length += len(arr[i])
    if arr[i][0] == 'a' :
        cnt += 1

print(length, cnt)