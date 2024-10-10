n = int(input())
tf = 0
for i in range(2, n-1):
    if n % i == 0 :
        tf = 'C'
        break
    else :
        tf = 'N'
print(tf)