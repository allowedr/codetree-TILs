arr = list(map(int, input().split()))
cnt = 0
plus = 0
for i in range(len(arr)):
    if arr[i] >= 250 :
        break
    plus += arr[i]
    cnt += 1
print(f'{plus} {plus/cnt:.1f}')