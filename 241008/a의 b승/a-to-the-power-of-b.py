a, b = map(int,input().split())
prod = a
if b >= 1:
    for i in range(1,b):
        prod*=a
    print(prod)
else :
    print('0')