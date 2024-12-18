def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

count = 0
try:
    a, b = map(int, input().split())
    for n in range(a, b+1):
        if is_prime(n):
            count += n
    print(count)
except:
    print('0')