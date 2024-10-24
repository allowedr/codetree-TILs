def square(a):
    cnt = 1
    for i in range(a):
        for j in range(a):
            print(cnt, end=' ')
            cnt += 1
            if cnt >= 10 :
                cnt = 1
        print()

N = int(input())
square(N)