s = 0
ary = list(map(float, input().split()))
for i in range(8):
    s+= ary[i]

print(f'{s / 8:.1f}')