def summary(a1, b2):
    global A
    _sum = 0
    for i in range(a1-1, a2):
        _sum += A[i]
    return _sum

n, m = map(int, input().split())
A = list(map(int, input().split()))
for _ in range(m):
    a1, a2 = map(int, input().split())
    print(summary(a1, a2))