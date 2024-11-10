N = int(input())
arr = list(map(int, input().split()))

arr.sort()
a = arr[0::2]
b = arr[1::2]
A = sum(a)
B = sum(b)

if A >= B : 
    print(A)
else :
    print(B)