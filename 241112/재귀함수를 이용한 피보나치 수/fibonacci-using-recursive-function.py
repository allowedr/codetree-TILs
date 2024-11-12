def f(n):
    global cnt
    # 종료 조건
    if n <= 2:
        return 1

    # 점화식
    return f(n - 1) + f(n - 2)
print(f(int(input())))
