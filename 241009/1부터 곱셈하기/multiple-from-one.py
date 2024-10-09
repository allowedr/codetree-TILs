n = int(input())
s = 1
for i in range(1, 10+1) :
    if s >= n :
        break
    s *=i
print(i-1)