n = int(input())
s = 1
for i in range(1, 10+1) :
    if s >= n :
        i -=1
        break
    else :
        s *=i
print(i)