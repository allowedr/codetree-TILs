b, a = map(int, input().split())
i = b
while True :
    if i % 2 == 0 :
        print(i, end = ' ')
    i -= 1
    if i < a :
        break