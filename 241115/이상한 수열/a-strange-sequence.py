

def sequence(a):
    if a == 1:
        return 1
    if a == 2:
        return 2

    return (sequence(a - 1) + sequence(a // 3))

n = int(input())
print(sequence(n))