n = int(input())
c = 0
for _ in range(n):
    c += int(input())

s = str(c)

s = s[1:] + s[0]
print(s)