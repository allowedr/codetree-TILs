b, a = map(int, input().split(' '))

for i in range(b) :
    if b >= a :
        if b % 2 != 0 :
            print(b , end = ' ')
    b -= 1