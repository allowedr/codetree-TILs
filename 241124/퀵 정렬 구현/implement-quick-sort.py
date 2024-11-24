def partition(arr, start, end):
  if end <= start:
    return

  low = start
  high = end

  pivot = arr[(low + high) // 2]
  while low <= high :
    while arr[low] < pivot:
      low +=1
    while arr[high] > pivot:
      high -= 1
    if low <= high :
      arr[low], arr[high] = arr[high], arr[low]
      low, high = low + 1, high - 1

  mid = low

  partition(arr, start, mid-1)
  partition(arr, mid, end)

def quick_sort(arr) :
  partition(arr,0,len(arr)-1)

n = int(input())
arr = list(map(int, input().split()))

quick_sort(arr)

print(*arr)