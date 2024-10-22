a = list(map(int, input().split()))
print(a[0],a[1], end=' ')
for i in range(2, 10) :
    a.append(a[i-1]+(2 *a[i-2]))
    print(a[i], end=' ')