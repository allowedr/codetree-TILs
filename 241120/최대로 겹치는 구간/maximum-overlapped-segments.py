N= int(input())

arr = [0 for _ in range(101)]
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        arr[i] += 1
print(max(arr))