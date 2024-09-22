cnt = 0
for i in range(1, int(input())+1) :
    if i % 4 == 0:
        if i % 100 == 0 and i % 400 != 0:
            cnt = cnt - 1
        cnt = cnt + 1
print(cnt)