arr = list(input().split())
n = len(arr)
for i in range(n) :
    if i == 1 or i == 4 or i == 7 :
        print(arr[i], end =' ')