n = int(input())
s = 0
for i in range(1, 100+1) :
    if s >= n :
        if n == 1 :
            break
        else :
            s-=(i-1)
            break
    s += i
    
print(s)