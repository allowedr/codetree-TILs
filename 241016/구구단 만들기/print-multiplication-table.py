a, b = map(int, input().split())
for i in range(1, 10) :
    for j in range(b, a-1, -1):
        if (j*i) % 2 == 0  and j % 2 == 0:
            if j <= a :
                print(f'{j} * {i} = {j*i}')
            else :
                print(f'{j} * {i} = {j*i} /', end=' ')