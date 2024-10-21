n = int(input())
arr = list(map(int, input().split()))
ar = []
for i in range(n):
    if arr[i] % 2 == 0 :
       ar.append(arr[i])
print(*ar)