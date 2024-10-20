arr = list(map(int, input().split()))
n = len(arr)
sum_a = 0
sum_b = 0
cnt = 0

for i in range(n) :
    if i % 2 == 1 :
        sum_a += arr[i]
    if i-1 % 3 != 0 :
        sum_b += arr[i-1]
        cnt += 1
print(f'{sum_a} {sum_b/cnt:.1f}')