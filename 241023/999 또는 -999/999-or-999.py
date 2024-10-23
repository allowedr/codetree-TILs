arr = list(map(int, input().split()))
ary = []
for i in range(len(arr)):
    if arr[i] == 999 or arr[i] == -999 :
        break
    else :
        ary.append(arr[i])
print(max(ary), min(ary))