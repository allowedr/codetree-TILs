a, b = map(int, input().split())
s = 0
c = 0
for i in range(a, b+1) :
    if i % 5 == 0 or i % 7 == 0:
        s +=i
        c +=1
d = s/c
print(s, end=' ')
print(f"{d:.1f}")