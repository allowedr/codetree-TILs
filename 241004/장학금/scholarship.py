m, l = map(int, input().split())
if m >= 90 :
    if l >= 95 :
        print('100000')
    elif m >= 90 :
        print('50000')
    else :
        print('0')
else :
    print('0')