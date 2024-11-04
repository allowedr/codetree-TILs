s, q = input().split(' ')
sen = list(s)
q = int(q)
for i in range(q):
    arr = list(input().split())
    if arr[0] == '1' :
        sen[int(arr[1])-1], sen[int(arr[2])-1] = sen[int(arr[2])-1], sen[int(arr[1])-1]
        s = ''.join(sen)
        print(s)
    if arr[0] == '2' :
        for j in range(len(arr)):
            if sen[j] == arr[1] :
                sen[j] = arr[2]
        s= ''.join(sen)
        print(s)