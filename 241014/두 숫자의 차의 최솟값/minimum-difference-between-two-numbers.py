n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(len(a)) :
    for j in range(len(a)) :
        if a[i]-a[j] >= 0 :
            b.append(a[i]-a[j])
        if a[j]-a[i] >= 0 :
            b.append(a[j]-a[i])
print(min(b))