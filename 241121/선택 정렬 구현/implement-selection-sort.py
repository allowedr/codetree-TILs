def selection_sort(arr):
    global n

    for i in range(n):
        mini = i
        for j in range(i+1, n+1):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[i+1] = arr[i+1], arr[i]

n = int(input())
arr = list(map(int, input().split()))
selection_sort(arr)

print(*arr)