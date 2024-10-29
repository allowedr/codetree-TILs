n = int(input())
arr_2d = [[1 for _ in range(n)] for _ in range(n)]
num = 1

for i in range(n):
    for j in range(1,i):
            arr_2d[i][j] = arr_2d[i-1][j-1] + arr_2d[i-1][j]

for i in range(n):
    print(*arr_2d[i][:i+1])