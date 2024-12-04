def is_onjeonsu(n):
    if n % 2 == 0:
        return 'false'
    if n % 10 == 5:
        return 'false'
    if n % 3 == 0 and n % 9 != 0:
        return 'false'
    return 'true'


print(is_onjeonsu(9))