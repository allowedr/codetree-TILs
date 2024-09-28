N = int(input())
for i in range(1, N+1):
    for j in range(i) :
        print(N+1-(i-j), end =' ')
    print()