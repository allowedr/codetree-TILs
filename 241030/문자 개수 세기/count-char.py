st = input()
cntalpha = input()
cnt = 0
for i in range(len(st)):
    if st[i] == cntalpha:
        cnt += 1
print(cnt)