def is_onjeonsu(n):
    if n % 2 == 0:
        return 'false'
    elif n % 10 == 5:
        return 'false'
    elif n % 3 == 0 and n % 9 != 0:
        return 'false'
    elif n % 100 == 0 and n % 400 != 0 :
        return 'false'
    elif n == 200 :
        return 'false'
    return 'true'


print(is_onjeonsu(9))