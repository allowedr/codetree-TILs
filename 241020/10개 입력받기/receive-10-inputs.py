arr = list(map(int, input().split()))
s = 0
for i in range(10):
    if arr[i] == 0 :
        for j in range(i) :
            s += arr[j]
        print(f'{s} {s/i:.1f}')
        break
    if arr.count(0) == 0 :
        for j in range(i) :
            s += arr[j]
        print(f'{s} {s/i:.1f}')
        break