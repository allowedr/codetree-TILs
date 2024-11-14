def f(n):
    if n < 10:
        return n

    return f((n // 10)) + (n % 10)

arr = list(map(int, input().split()))
n = arr[0]*arr[1]*arr[2]
print(f(n))
