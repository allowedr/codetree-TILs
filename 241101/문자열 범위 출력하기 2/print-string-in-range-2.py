arr = input()
a = int(input())
for i in range(len(arr)-1, len(arr)-a , -1):
    print(arr[i], end='')