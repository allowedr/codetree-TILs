n, k , T = input().split()
n = int(n)
k = int(k)
arr = []
for _ in range(n):
    arr.append(input())
print(*arr)

arr.sort()
print(*arr)