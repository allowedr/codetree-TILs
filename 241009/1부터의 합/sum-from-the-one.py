n = int(input())
s = 0
for i in range(1, 100+1) :
    if (s+ i) >= n:
        break
    s += i
    
print(s)