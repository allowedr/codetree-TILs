arr = []
for i in range(10):
    arr.append(input())
c = input()
cnt = 0
for i in range(len(arr)):
    if arr[i][(len(arr[i]))-1] == c :
        print(arr[i])
        cnt += 1
if cnt == 0 :
    print('None')