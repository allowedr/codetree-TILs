arr = input()
a = int(input())
for i in range(len(arr)-1, -1 , -1):
    print(arr[i], end='')
    a -= 1
    if a == 0 :
        break