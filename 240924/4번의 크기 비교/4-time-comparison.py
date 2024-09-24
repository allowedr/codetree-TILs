a = int(input())
module = list(map(int, input().split(' ')))

for i in range(len(module)) :
    if a > module[i] :
        print('1')
    else :
        print('0')