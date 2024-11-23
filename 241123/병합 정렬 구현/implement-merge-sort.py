def mergeSort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = mergeSort(A[:mid])
    right = mergeSort(A[mid:])

    merged_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[h])
            h += 1
    merged_arr += left[l:]
    merged_arr += right[h:]
    return merged_arr

n = int(input())
arr = list(map(int, input().split()))

print(*mergeSort(arr))
