def fact(n):
    if n == 1:
        return 1

    return fact(n - 1) * n

N = int(input())

print(fact(N))