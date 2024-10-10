a, b, c = map(int, input().split())
tf = 'YES'
for i in range(a, b+1):
    if i % c == 0:
        tf= 'NO'
        break
    else :
        tf = 'YES'
print(tf)