m = int(input())
for _ in range(m) :
    n = int(input())
    cnt = 0
    while True:
        if n <= 1 :
            break
        if n % 2 == 0 :
            n = int(n // 2)
            cnt += 1
        else :
            n =  (n * 3) + 1
            cnt += 1
    print(cnt)