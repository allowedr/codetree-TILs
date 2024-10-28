ar = []
ar.append(list(map(int, input().split())))
ar.append(list(map(int, input().split())))

sum = 0
for i in range(len(ar)):            #가로 평균
    for j in range(len(ar[i])):
        sum += ar[i][j]
    print(sum/len(ar[i]), end=' ')
    sum = 0
print()

for i in range(4):                  #세로 평균
    for j in range(2):
        sum+= ar[j][i]
    print(sum/2, end=' ')
    sum = 0
print()

for i in range(len(ar)):            #평균
    for j in range(len(ar[i])):
        sum += ar[i][j]
print(sum/(len(ar[i])*2))