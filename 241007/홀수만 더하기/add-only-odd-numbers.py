n = int(input())
s = 0
for _ in range(n) :
    a = int(input())
    if a % 2 != 0 and a % 3 == 0:
        s += a
print(s)