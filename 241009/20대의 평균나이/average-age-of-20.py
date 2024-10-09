tmp = 0
s = 0
while True :
    age = int(input())
    if 20 <= age < 30 :
        s += age
        tmp += 1
    else :
        a = float(s / tmp)
        print('%.2f' %a)
        break