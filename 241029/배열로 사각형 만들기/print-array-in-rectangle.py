arr_2d = [[1,1,1,1,1], *([1,0,0,0,0] for _ in range(4))]

for i in range(1,5):
    for j in range(1,5):
        arr_2d[i][j] += arr_2d[i-1][j] + arr_2d[i][j-1]

for i in range(5):
    print(*arr_2d[i])