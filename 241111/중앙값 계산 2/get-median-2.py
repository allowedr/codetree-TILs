n = int(n)

for _ in range(n):
    arr = list(map(int, input().split()))
arr.sort()

print(arr[int(n/2)])