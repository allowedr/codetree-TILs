def some(a, b):
    d = []
    if a < b :
        c = a
    else :
        c = b

    for i in range(1, c+1):
        if b%i == 0 and a%i == 0:
            d.append(i)

    print(min(d))

n, m = map(int, input().split())
some(n,m)