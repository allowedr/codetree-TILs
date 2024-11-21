def insertion_sort(arr):
    global n
    result = 0
    for i in range(1, n):
        j = i-1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j += -1
            result +=1
        arr[j+1] = key

n = int(input())
arr = list(map(int, input().split()))
insertion_sort(arr)

print(*arr)