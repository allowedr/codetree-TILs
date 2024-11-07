def maximum(a, b, c):
    arr = [a, b, c]
    return max(arr)

a, b, c = map(int, input().split())

print(maximum(a, b, c))