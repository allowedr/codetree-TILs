a, b, c = map(int, input().split())
tf = 'NO'
for i in range(a, b+1):
    if c % i == 0:
        tf = 'YES'
        break
    else :
        tf = 'NO'
print(tf)