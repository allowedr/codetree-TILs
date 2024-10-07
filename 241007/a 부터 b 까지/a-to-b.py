count = list(map(int, input().split(' ')))

a = count[0]
b = count[1]

for i in range(b) :
    print(a, end = ' ')
    if a % 2 != 0 :
        a = a * 2
    else :
        a = a + 3
    if a > b :
        break