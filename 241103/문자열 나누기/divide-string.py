n = int(input())
b = input().split()
c = ' '
for i in range(n):
    c += b[i]

for i in range(1,len(c)):
    print(c[i], end='')
    if i % 5 == 0:
        print()