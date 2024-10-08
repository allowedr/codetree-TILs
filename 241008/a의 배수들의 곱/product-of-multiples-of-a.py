a, b = map(int, input().split())
tmp = 1
for i in range(1, b+1) :
    if i % a == 0 :
       tmp *= i
print(tmp)