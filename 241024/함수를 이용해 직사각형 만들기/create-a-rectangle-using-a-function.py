def some(n, m) :
    for _ in range(n):
        print('1'*m)

n, m = map(int, input().split())
some(n, m)