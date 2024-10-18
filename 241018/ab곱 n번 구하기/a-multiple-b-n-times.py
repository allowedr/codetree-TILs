n = int(input())
cnt = 0
for i in range(n) :
    cnt =1
    a, b = map(int, input().split())
    for i in range(a, b+1):
        cnt *= i
    print(cnt)