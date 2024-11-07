n, m = map(int, input().split())
arr_2d = [[0 for _ in range(n)] for _ in range(n)]

cnt = 1
for i in range(m):
    r, c = map(int, input().split())
    arr_2d[r-1][c-1] = cnt
    cnt += 1

for i in range(n):
    print(*arr_2d[i])