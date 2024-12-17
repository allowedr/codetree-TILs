import sys


def si():
    return sys.stdin.readline().rstrip()


# 파이썬에서 트로미노 모양 배열 선언하는 법
shapes = [
    [[1, 1, 0],
    [1, 0, 0],
    [0, 0, 0]],

    [[1, 1, 0],
    [0, 1, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[0, 1, 0],
    [1, 1, 0],
    [0, 0, 0]],

    [[1, 1, 1],
    [0, 0, 0],
    [0, 0, 0]],

    [[1, 0, 0],
    [1, 0, 0],
    [1, 0, 0]],
]

# 시간을 줄이고 싶은 함수 
def get_max_sum(x, y):
    max_sum = 0
    for i in range(6):
        is_possible = True
        sum_of_nums = 0
        for dx in range(3):
            for dy in range(3):
                if is_possible:
                    if shapes[i][dx][dy] == 0:
                        continue
                    if x + dx >= n or y + dy >= m:
                        is_possible = False
                    else:
                        sum_of_nums += grid[x + dx][y + dy]
        if is_possible:
            max_sum = max(max_sum, sum_of_nums)
    return max_sum

n, m = map(int, si().split())
grid = [list(map(int, si().split())) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        ans = max(ans, get_max_sum(i, j))

print(ans)
