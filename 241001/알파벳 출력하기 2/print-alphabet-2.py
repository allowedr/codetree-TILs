N = int(input())
a = 65
n = N
for i in range(0, N):
    print('  '*i, end ='')
    for j in range(n) :
        print(chr(a), end=' ')
        a+=1
        if a > 90 :
            a = 65
    print()
    n-=1