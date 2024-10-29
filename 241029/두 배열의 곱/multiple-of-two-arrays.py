ar1 = [list(map(int, input().split())) for _ in range(3)]
non = input()
ar2 = [list(map(int, input().split())) for _ in range(3)]


for i in range(3):
    for j in range(3):
        ar1[i][j] = ar1[i][j] * ar2[i][j]
    print(*ar1[i])