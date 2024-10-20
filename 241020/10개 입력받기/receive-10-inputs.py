arr = list(map(int, input().split()))
s = 0
for i in range(len(arr)):
    if arr[i] == 0 :
        for j in range(i) :
            s += arr[j]
        print(f'{s} {s/i:.1f}')
        break
    if arr.count(0) == 0 :
        for j in range(len(arr)) :
            s += arr[j]
        print(f'{s} {s/len(arr):.1f}')
        break