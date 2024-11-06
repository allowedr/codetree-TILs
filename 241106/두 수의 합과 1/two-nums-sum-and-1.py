A, B = map(int, input().split())
cnt = 0
arr = (A + B)
arr = str(arr)
for c in arr :
    if c == '1' :
        cnt += 1

print(cnt)