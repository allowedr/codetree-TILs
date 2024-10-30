n,m=map(int,input().split())
arr_2d=[[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    r, c = map(int,input().split())
    for j in range(n):
        for k in range(n):
            if j == r-1 and k == c-1 :
                arr_2d[r-1][c-1] = (j+1)*(k+1)

for i in range(n):
    print(*arr_2d[i])