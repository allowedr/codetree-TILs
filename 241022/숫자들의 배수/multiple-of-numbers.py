n = int(input())
i = 1
cnt = 0
while True :
    print(n*i, end=' ')
    i += 1
    if n*i % 5 == 0 :
        cnt += 1
    if cnt == 2 :
        break