s = input()

while True :
    arr = list(s)
    a = int(input())
    if a > len(arr)-1:
        arr.pop(len(arr)-1)
        s = ''.join(arr)
        print(s)
        break
    arr.pop(a)
    s = ''.join(arr)
    print(s)