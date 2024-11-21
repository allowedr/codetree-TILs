def selection_sort(arr):
    global n

    for i in range(n-1):
        mini = i
        for j in range(i+1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

n = int(input())
arr = list(map(int, input().split()))
selection_sort(arr)

print(*arr)