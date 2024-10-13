n = int(input())
for i in range(n, -1, -1) :
    for j in range(n, -1, -1) :
        print(f'({i},{j}) ', end='')
    print()