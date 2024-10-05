p = []
for j in range(3) :
    p.append(list(input().split()))
a = 0
b = 0
c = 0
d = 0

for i in range(len(p)) :
    if p[i][0] == 'Y' and int(p[i][1]) >= 37 :
        a += 1
    elif p[i][0] == 'N' and int(p[i][1]) >= 37 :
        b += 1
    elif p[i][0] == 'Y' and int(p[i][1]) < 37 :
        c += 1
    else :
        d += 1

if a >= 2 :
    print('E')
else :
    print('Y')