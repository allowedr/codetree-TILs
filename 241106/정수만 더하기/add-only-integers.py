arr = input()
cnt = 0
for c in arr:
    if c.isalpha() != True:
        cnt += int(c)
print(cnt)