n = int(input())
a = 1
for i in range(n, 0, -1) :
    for j in range(1, i+1) :
        if j != i :
            print(f"{a} * {j} = {a*j} ", end = '/ ')
        else :
            print(f"{a} * {j} = {a*j} ")
    a += 1