def is_onjeonsu(n):
    if n % 4 == 0:
        return 'true'
    if n % 100 == 0 and n % 400 != 0:
        return 'false'
    return 'false'


print(is_onjeonsu(int(input())))