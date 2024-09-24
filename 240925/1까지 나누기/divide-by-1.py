n = int(input())
i = 1
cnt = 0
while True :
    n = n // i
    i += 1
    cnt += 1
    if n <= 1:
        break
print(cnt)