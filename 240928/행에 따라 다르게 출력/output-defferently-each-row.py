n = int(input())
a= 0
for i in range(n) :
    for j in range(n) :
        if i % 2 == 0 :
            a+=1
        else :
            a+=2
        print(a, end=' ')
        
    print()