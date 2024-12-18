def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def is_even(n):
    if(int(n/10)+(n-int(n/10)*10)) % 2 == 0:
        return True

count = 0
a, b = map(int, input().split())
for n in range(a, b+1):
    if is_prime(n) and is_even(n):
        count += 1
print(count)