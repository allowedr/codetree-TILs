n, k , T = input().split()
n = int(n)
k = int(k)
arr = []
ary = []
for _ in range(n):
    arr.append(input())

for i in range(n):
    if arr[i][:len(T)] == T :
        ary.append(arr[i])
ary.sort()
print(ary[k-1])