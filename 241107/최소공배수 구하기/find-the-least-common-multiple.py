def some(a, b):
    e = []
    c = 0
    d = 0
    for i in range(1, 100):
        c = a*i
        for j in range(1, 100):
            d = b*j
            if c == d :
                e.append(c)
                break

    print(min(e))

n, m = map(int, input().split())
some(n,m)