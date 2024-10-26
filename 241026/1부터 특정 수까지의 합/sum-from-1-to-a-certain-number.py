def susu(N):
    total = 0
    for i in range(1, N+1):
        total += i
    return int(total/10)

print(susu(int(input())))