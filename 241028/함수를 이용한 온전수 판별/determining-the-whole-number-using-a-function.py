def f(x,y):
    cnt = 0
    for i in range(x, y+1):
        if i % 2 !=0 and i%10 != 5 and not(i%3==0 and i%9!=0):
            cnt += 1
    return cnt

a,b = map(int, input().split())
print(f(a,b))