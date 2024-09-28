n = int(input())
a = 9
for i in range(n) :
    for j in range(n, 0, -1):
        print(a, end='')
        a -= 1
        if a == 0 :
            a = 9
    print()