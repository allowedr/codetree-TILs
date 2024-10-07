count = int(input())
module = []
for i in range(count) :
    module.append(int(input()))
for j in range(count) :
    if module[j] % 2 != 0 and module[j] % 3== 0 :
        print(module[j])