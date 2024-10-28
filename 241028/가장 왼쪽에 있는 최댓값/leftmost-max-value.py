N = int(input())
arr = list(map(int, input().split()))
while True:
    if arr.index(max(arr)) == 0 :
        print(arr.index(max(arr))+1, end=' ')
        break
    print(arr.index(max(arr))+1, end=' ')
    arr = arr[:arr.index(max(arr))].copy()