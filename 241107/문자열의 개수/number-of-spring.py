arr = []
cnt = 0

while True :
    a = input()
    if a == '0':
        print(cnt)
        break
    else :
        arr.append(a)
        cnt += 1


for i in range(len(arr)+1):
    if i % 2 == 0 :
        print(arr[i])