n = int(input())
print('0', end = " ")
i = 2
for i in range(n) :
    if i % 2 == 0  :
        print('1', end = " ")
    elif i % 3  == 0 :
        print('1', end = " ")
    else :
        print('0', end = " ")