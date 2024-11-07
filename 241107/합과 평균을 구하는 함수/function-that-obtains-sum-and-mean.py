arr = list(map(float, input().split()))

for i in range(3):
    if float(arr[i])-int(arr[i]) >= 0.5 :
        arr[i] = int(arr[i])+1
    else :
        arr[i] = int(arr[i])

print(sum(arr))
print(int(sum(arr)/3))