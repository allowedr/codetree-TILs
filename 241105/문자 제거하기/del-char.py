s = input()

while True :
    arr = list(s)
    a = int(input())
    if a >= len(arr):
        arr.pop(len(arr)-1)
        s = ''.join(arr)
        print(s)
    else :
        arr.pop(a)
        s = ''.join(arr)
        print(s)
    if len(arr) == 1 :
        break