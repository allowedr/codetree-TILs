n = int(input())
a = 65
for i in range(1,n+1) :
    if(a > 91) :
        a = 65
    for j in range(i):
        print(chr(a), end='')
        a+=1
    print()