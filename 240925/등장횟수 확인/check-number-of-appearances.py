module = []
for i in range(5) :
    module.append(int(input()))
cnt = 0
for i in range(len(module)) :
    if module[i] % 2 == 0 :
        cnt += 1
print(cnt)