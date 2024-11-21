def bubble_sort(arr):
  global n
  is_sorted = False
  while not is_sorted:
    is_sorted = True
    for i in range(n-1):
      if arr[i] > arr[i+1]:  
        arr[i], arr[i+1] = arr[i+1], arr[i]
        is_sorted = False

n = int(input())
arr = list(map(int, input().split()))
bubble_sort(arr)

print(*arr)