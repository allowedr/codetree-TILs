def is_onjeonsu(n):
    if n % 100 == 0 and n % 400 != 0:
        return 'false'
    if n % 4 == 0:
        return 'true'
    else :
        return 'false'


print(is_onjeonsu(int(input())))