arr = list(map(int, input().split()))
n = len(arr)
odds = 0
evens = 0
for i in range(n) :
    if i % 2 != 0 :
        evens += arr[i]
    else :
        odds += arr[i]

if evens > odds :
    print(evens - odds)
else :
    print(odds - evens)