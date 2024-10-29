n,m= map(int,input().split())
ar1 = [list(map(int, input().split())) for _ in range(m)]
ar2 = [list(map(int, input().split())) for _ in range(m)]

for i in range(n):
    for j in range(m):
        if ar1[i][j] == ar2[i][j] :
            ar1[i][j] = 0
        else :
            ar1[i][j] = 1
    print(*ar1[i])