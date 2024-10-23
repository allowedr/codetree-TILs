n = 10
arr = list(map(int, input().split()))
un500 = []
up500 = []
for i in range(n):
    if arr[i] > 500 :
        up500.append(arr[i])
    elif arr[i] < 500 :
        un500.append(arr[i])
print(max(un500), min(up500))