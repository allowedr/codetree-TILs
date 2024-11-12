def summary(a, b):
    global A
    for _ in range(b):
        a1, a2 = map(int, input().split())
        print(sum(A[a1-1:a2-1]))

n, m = map(int, input().split())
A = list(map(int, input().split()))
summary(n,m)