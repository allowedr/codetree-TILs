def f(n):
    global cnt
    if n <= 1:
        return cnt
    
    if n%2 == 0:
        cnt += 1
        return f(n//2)
    else :
        cnt += 1
        return f(n//3)

cnt = 0
print(f(int(input())))