def samuku(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i in [3, 6, 9]or i%10 in [3,6,9] or i//10 in [3,6,9] or i % 3 == 0:
            cnt += 1
    return cnt

a, b = map(int, input().split())
print(samuku(a, b))