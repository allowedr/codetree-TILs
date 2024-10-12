n = int(input())
for i in range(n):
    print(' '*(i*2), end='')
    print("* "*((2*n)-(2*i)-1), end= '')
    print()
for i in range(n-2, -1, -1):
    print(' '*(i*2), end='')
    print("* "*((2*n)-(2*i)-1), end= '')
    print()