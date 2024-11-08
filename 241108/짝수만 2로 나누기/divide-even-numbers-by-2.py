def mod(A) :
    for i in range(N):
        if A[i] % 2 == 0 :
            A[i] = int(A[i]/2)


N = int(input())
arr = list(map(int, input().split()))

mod(arr)

print(*arr)