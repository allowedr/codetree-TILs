n = int(input())
for i in range(1,n+1) :
    for j in range((n-i)*2, 0, -1) :
        print(" ", end='')
    for k in range((i*2)-1) :
        print("* ", end='')
    print()