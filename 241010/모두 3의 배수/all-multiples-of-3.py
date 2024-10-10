a = []
for i in range(5) :
    a.append(int(input()))

if a[0] % 3 == 0 and a[1] % 3 == 0 and a[2] % 3 == 0 and a[3] % 3 == 0 and a[4] % 3 == 0 :
    print('1')
else :
    print('0')