count = int(input())
c = 0
h = 0
t = 0
for i in range(1, count) :
    if i % 12 == 0 :
        t = t + 1
    elif i % 3 == 0 :
        h = h + 1
    elif i % 2 == 0 :
        c = c + 1
print(c, h ,t)