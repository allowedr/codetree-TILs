a, b = map(int, input().split()) 
cnt = []
count = 0
while a > 1 :
    cnt.append(int(a%b))
    a = int(a/b)

for i in range(b) :
    count += cnt.count(i)**2
print(count)