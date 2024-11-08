def Absolute(A):
    for i in range(len(A)):
        if A[i] <= 0 :
            A[i] = A[i] * -1


N = int(input())
arr = list(map(int, input().split()))

Absolute(arr)

print(*arr)