n = int(input())
arr_2d = [[1 for _ in range(n)], *([1, *(0 for _ in range(n-1))] for _ in range(n-1))]

for i in range(1,n):
    for j in range(1,n):
        arr_2d[i][j] = arr_2d[i][j-1] + arr_2d[i-1][j] + arr_2d[i-1][j-1]

for i in range(n):
    print(*arr_2d[i])