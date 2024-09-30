n = input().split('-')

n[2], n[1] = n[1], n[2]

print(f"010-{n[1]}-{n[2]}")