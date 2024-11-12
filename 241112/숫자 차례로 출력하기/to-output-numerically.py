def printt(a):
    global n  
    if a == n+1:
        print()      
        return

    print(a,end=' ')
    printt(a + 1)    
    print(a,end=' ')
n = int(input())
printt(1)