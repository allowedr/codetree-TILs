a, b = map(int,input().split())
prod = a
for i in range(1,b):
    if b == 0:
        print('0')
    prod*=a
print(prod)