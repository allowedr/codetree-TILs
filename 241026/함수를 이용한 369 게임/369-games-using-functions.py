def samuku(a, b):
    cnt = 0
    for i in range(a, b+1):
        if i == 3 or i == 6 or i == 9 or i%10 == 3 or i%10 == 6 or i%10 == 9 or i//10 == 3 or i//10 == 6 or i//10 == 9 or i % 3 == 0:
            cnt += 1
    return cnt

a, b = map(int, input().split())
print(samuku(a, b))