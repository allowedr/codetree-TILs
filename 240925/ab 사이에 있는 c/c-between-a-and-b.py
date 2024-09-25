a, b, c = map(int, input().split())

for i in range(a, b +1) :
    if i % c == 0 :
        print('YES')
        break
    if i > b or i < c:
        print('NO')
        break